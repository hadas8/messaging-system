from django.contrib import admin

# Register your models here.
from .models import Message, UserMessageStatus

admin.site.register(Message)
admin.site.register(UserMessageStatus)
