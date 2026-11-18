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


class IsVerifiedBrandOrReadOnly(permissions.BasePermission):
    """
    - Lasīt (GET) var visi.
    - Izveidot/mainīt var tikai verificēti zīmoli (brand_profile.is_verified=True) vai staff/admin.
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

        brand_profile = getattr(user, "brand_profile", None)
        return bool(
            getattr(user, "role", None) == "brand"
            and brand_profile is not None
            and brand_profile.is_verified
        )

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return getattr(obj, "brand", None) == request.user or request.user.is_staff


class IsEligibleAthlete(permissions.BasePermission):
    """
    Atļauj piekļuvi tikai autentificētiem sportistiem, kuriem ir profils un kuri nav nobanoti.
    """

    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated or getattr(user, "role", None) != "athlete":
            return False

        athlete_profile = getattr(user, "athlete_profile", None)
        return bool(athlete_profile is not None and not athlete_profile.is_banned)