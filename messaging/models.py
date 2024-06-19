from django.db import models
from django.contrib.auth.models import User 


class Message(models.Model):
    """
    Model representing a message between users.
    """
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    subject = models.CharField(max_length=255, help_text='Enter the subject of the message.')
    message = models.TextField(help_text='Enter the content of the message.')
    creation_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """
        String for representing the Message object (subject).
        """
        return self.subject


class UserMessageStatus(models.Model):
    """
    Model representing the status of a message for a specific user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'message')
