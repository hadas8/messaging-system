from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Message, UserMessageStatus


class MessageSerializer(serializers.ModelSerializer):
    """
    Serializer for the Message model.
    """
    sender = serializers.ReadOnlyField(source='sender.username')
    receiver = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'subject', 'message', 'creation_date']
        read_only_fields = ['creation_date']


class UserMessageStatusSerializer(serializers.ModelSerializer):
    """
    Serializer for the UserMessageStatus model.
    """
    message = MessageSerializer()
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UserMessageStatus
        fields = ['id', 'user', 'message', 'is_read', 'is_deleted']