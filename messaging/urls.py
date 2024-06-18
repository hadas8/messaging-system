from django.urls import path
from .views import (
    MessageCreateView,
    SentMessagesListView,
    ReceivedMessagesListView,
    UnreadMessagesListView,
    MessageDetailView
)

urlpatterns = [
    path('write/', MessageCreateView.as_view(), name='write-message'),
    path('sent/', SentMessagesListView.as_view(), name='sent-messages'),
    path('all/', ReceivedMessagesListView.as_view(), name='get-all-messages'),
    path('unread/', UnreadMessagesListView.as_view(), name='get-unread-messages'),
    path('<int:pk>/', MessageDetailView.as_view(), name='read-message'),
]
