from dj_rest_auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    UserDetailsView,
)


login = LoginView.as_view()
logout = LogoutView.as_view()
password_change = PasswordChangeView.as_view()
user_details = UserDetailsView.as_view()
