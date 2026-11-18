from rest_framework import permissions


class IsAdminOrStaffOrReadOnly(permissions.BasePermission):
    """
    Allows anyone to read (GET, HEAD, OPTIONS),
    but restricts write actions (POST, PUT, PATCH, DELETE) to staff and superusers.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)