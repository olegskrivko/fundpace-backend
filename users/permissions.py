from rest_framework import permissions


class IsAdminOrStaffOrReadOnly(permissions.BasePermission):
    """
    Allows anyone to read (GET, HEAD, OPTIONS),
    but restricts write actions (POST, PUT, PATCH, DELETE) to staff and superusers.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(
            request.user and request.user.is_authenticated and request.user.is_staff
        )


class IsVerifiedBrandOrReadOnly(permissions.BasePermission):
    """
    - Lasīt (GET) var visi.
    - Izveidot/mainīt var tikai verificēti zīmoli vai staff/admin.
    - Objekta līmenī mainīt var tikai īpašnieks (obj.brand) vai staff/admin.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        user = request.user
        if not user or not user.is_authenticated:
            return False

        if user.is_staff:
            return True

        return (
            getattr(user, "role", None) == "brand"
            and getattr(user, "is_verified_brand", False)
        )

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return getattr(obj, "brand", None) == request.user or request.user.is_staff


class IsAthlete(permissions.BasePermission):
    """Atļauj piekļuvi tikai autentificētiem sportistiem (noderēs pieteikumu aplikācijai)."""

    def has_permission(self, request, view):
        user = request.user
        return bool(
            user
            and user.is_authenticated
            and getattr(user, "role", None) == "athlete"
        )