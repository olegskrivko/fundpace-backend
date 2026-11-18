from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ["username", "email", "role", "company_name", "is_verified_brand", "is_staff"]
    list_filter = ["role", "is_verified_brand", "is_staff", "is_active"]
    search_fields = ["username", "email", "company_name", "first_name", "last_name"]
    
    # Pievienojam jaunos laukus Django Admin rediģēšanas skatam
    fieldsets = UserAdmin.fieldsets + (
        ("FundPace Role & Verification", {
            "fields": ("role", "company_name", "is_verified_brand"),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("FundPace Role & Verification", {
            "fields": ("role", "company_name", "is_verified_brand"),
        }),
    )