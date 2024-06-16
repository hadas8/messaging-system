from dataclasses import fields
from email import message
from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    """
    Serializer for the Message model.
    """
    class Meta:
        model = Message
        fields = [
            'id',
            'sender',
            'receiver',
            'subject',
            'message',
            'creation_date',
            'is_read'
        ]