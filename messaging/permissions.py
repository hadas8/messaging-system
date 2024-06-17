from rest_framework.permissions import BasePermission

class IsReceiver(BasePermission):
    """
    Custom permission to only allow receivers of a message to view it.
    """
    def has_object_permission(self, request, obj):
        # Only allow access if the user is the receiver of the message
        return obj.receiver == request.user