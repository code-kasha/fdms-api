from django.contrib import admin
from .models import Image, Gallery


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "slug",
        "image",
        "created_at",
        "updated_at",
        "deleted",
    )
    list_filter = ("created_at", "updated_at", "deleted")
    search_fields = ("slug",)
    date_hierarchy = "created_at"


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "updated_at", "deleted")
    list_filter = ("created_at", "updated_at", "deleted")
    date_hierarchy = "created_at"
