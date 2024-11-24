from django.urls import path

from .views import add_to_gallery

urlpatterns = [
    path("add/", add_to_gallery, name="add_to_gallery"),
]
