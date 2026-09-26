from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User, Profile


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("email", "is_staff", "is_active", "is_verified")
    list_filter = ("email", "is_staff", "is_active", "is_verified")
    search_fields = ("email",)
    ordering = ("email",)

    fieldsets = (
        ("authentication", {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_verified")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_verified",
                    "is_active",
                    "is_superuser",
                    "type",
                ),
            },
        ),
    )


class CustomProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "first_name", "last_name", "phone_number")
    searching_fields = (
        "user",
        "first_name",
        "last_name",
    )


admin.site.register(Profile, CustomProfileAdmin)
admin.site.register(User, CustomUserAdmin)
