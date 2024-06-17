from django.urls import path
from .views import (
    WriteMessageView,
    GetAllMessagesForUserView,
    GetUnreadMessagesForUserView,
    ReadMessageView,
    DeleteMessageView,
)

urlpatterns = [
    path('write/', WriteMessageView.as_view(), name='write-message'),
    path('', GetAllMessagesForUserView.as_view(), name='get-all-messages'),
    path('unread/', GetUnreadMessagesForUserView.as_view(), name='get-unread-messages'),
    path('<int:pk>/', ReadMessageView.as_view(), name='read-message'),
    path('<int:pk>/delete/', DeleteMessageView.as_view(), name='delete-message'),
]
