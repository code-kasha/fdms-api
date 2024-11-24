from django.contrib import admin

# Register your models here.
from .models import Farmer


@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "relative",
        "date_of_birth",
        "verified",
    )
    list_filter = ("date_of_birth", "verified")
    search_fields = ("name",)
