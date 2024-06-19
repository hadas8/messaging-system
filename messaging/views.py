from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.http import Http404

from .models import Message, UserMessageStatus
from .serializers import MessageSerializer, UserMessageStatusSerializer


class MessageCreateView(generics.CreateAPIView):
    """
    API view to create a new message.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Associates the message with the currently authenticated user as the sender
        and creates UserMessageStatus entries for the sender and receiver.
        """
        sender = self.request.user
        message = serializer.save(sender=sender)
        receiver = User.objects.get(username=serializer.validated_data['receiver'].username)
        
        # Create status for sender
        UserMessageStatus.objects.create(user=sender, message=message, is_read=True)

        # Create status for receiver
        UserMessageStatus.objects.create(user=receiver, message=message)


class SentMessagesListView(generics.ListAPIView):
    """
    API view to list all sent messages of the authenticated user.
    """
    serializer_class = UserMessageStatusSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Returns sent messages by the authenticated user that are not deleted.
        """
        user = self.request.user
        return UserMessageStatus.objects.filter(user=user, message__sender=user, is_deleted=False)


class ReceivedMessagesListView(generics.ListAPIView):
    """
    API view to list all received messages of the authenticated user.
    """
    serializer_class = UserMessageStatusSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Returns received messages by the authenticated user that are not deleted.
        """
        user = self.request.user
        return UserMessageStatus.objects.filter(user=user, message__receiver=user, is_deleted=False)


class UnreadMessagesListView(generics.ListAPIView):
    """
    API view to list all unread messages of the authenticated user.
    """
    serializer_class = UserMessageStatusSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Returns unread messages for the authenticated user that are not deleted.
        """
        user = self.request.user
        return UserMessageStatus.objects.filter(user=user, message__receiver=user, is_read=False, is_deleted=False)


class MessageDetailView(generics.RetrieveDestroyAPIView):
    """
    API view to retrieve or delete a specific message.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """
        Retrieves the specific message instance.
        """
        obj = super().get_object()
        user = self.request.user
        try:
            user_message_status = UserMessageStatus.objects.get(user=user, message=obj, is_deleted=False)
        except UserMessageStatus.DoesNotExist:
            raise Http404

        if not user_message_status.is_read:
            user_message_status.is_read = True
            user_message_status.save()

        return obj

    def perform_destroy(self, instance):
        """
        Marks the message as deleted for the authenticated user.
        Deletes the UserMessageStatus entry if both users have marked it as deleted.
        """
        user = self.request.user
        user_message_status = UserMessageStatus.objects.get(user=user, message=instance)
        user_message_status.is_deleted = True
        user_message_status.save()

        # Check if both sender and receiver have marked the message as deleted
        sender_status = UserMessageStatus.objects.get(user=instance.sender, message=instance)
        receiver_status = UserMessageStatus.objects.filter(message=instance).exclude(user=instance.sender).first()

        if sender_status.is_deleted and receiver_status.is_deleted:
            instance.delete()
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)