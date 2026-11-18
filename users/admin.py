from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AthleteProfile, BrandProfile, User


class AthleteProfileInline(admin.StackedInline):
    model = AthleteProfile
    can_delete = False
    extra = 0


class BrandProfileInline(admin.StackedInline):
    model = BrandProfile
    can_delete = False
    extra = 0


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = [
        "username",
        "email",
        "role",
        "get_verified_or_banned",
        "is_staff",
        "is_active",
    ]
    list_filter = [
        "role",
        "is_staff",
        "is_active",
        "brand_profile__is_verified",
        "athlete_profile__is_banned",
    ]
    search_fields = ["username", "email", "brand_profile__company_name"]
    inlines = [AthleteProfileInline, BrandProfileInline]

    fieldsets = UserAdmin.fieldsets + (
        ("FundPace Role", {"fields": ("role",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("FundPace Role", {"fields": ("role",)}),
    )

    @admin.display(description="Status")
    def get_verified_or_banned(self, obj):
        if obj.role == User.Role.BRAND and hasattr(obj, "brand_profile"):
            return (
                "Verified"
                if obj.brand_profile.is_verified
                else "Pending Verification"
            )
        if obj.role == User.Role.ATHLETE and hasattr(obj, "athlete_profile"):
            return "BANNED" if obj.athlete_profile.is_banned else "Active"
        return "-"