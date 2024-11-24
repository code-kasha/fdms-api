from django.urls import path

from .views import login, logout, password_change, user_details

urlpatterns = [
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("password/change/", password_change, name="password_change"),
    path("user/", user_details, name="user_details"),
]
