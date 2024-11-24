from django.contrib import admin

# Register your models here.

from .models import Token


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "issue",
        "content",
        "created_at",
        "updated_at",
        "status",
    )
    list_filter = ("user", "created_at", "updated_at", "status")
    date_hierarchy = "created_at"
