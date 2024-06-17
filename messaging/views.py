from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.authentication import SessionAuthentication
from .models import Message
from .serializers import MessageSerializer
from .permissions import IsReceiver
from django.shortcuts import get_object_or_404
from django.db.models import Q

class WriteMessageView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

class GetAllMessagesForUserView(generics.ListAPIView):
    serializer_class = MessageSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated, IsReceiver]

    def get_queryset(self):
        return Message.objects.filter(Q(receiver=self.request.user))

class GetUnreadMessagesForUserView(generics.ListAPIView):
    serializer_class = MessageSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated, IsReceiver]

    def get_queryset(self):
        return Message.objects.filter(receiver=self.request.user, is_read=False)

class ReadMessageView(generics.RetrieveAPIView):
    serializer_class = MessageSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated, IsReceiver]

    def get_queryset(self):
        return Message.objects.filter(Q(sender=self.request.user) | Q(receiver=self.request.user))

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['pk'])
        # Mark message as read if the current user is the receiver
        if self.request.user == obj.receiver:
            obj.is_read = True
            obj.save()
        return obj

class DeleteMessageView(generics.DestroyAPIView):
    serializer_class = MessageSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated, IsReceiver]

    def get_queryset(self):
        return Message.objects.filter(Q(sender=self.request.user) | Q(receiver=self.request.user))

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user == instance.sender or request.user == instance.receiver:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
