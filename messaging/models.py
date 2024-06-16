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
    is_read = models.BooleanField(default=False, help_text='Specifies whether the message has been read.')

    def __str__(self):
        """
        String for representing the Message object (subject).
        """
        return self.subject