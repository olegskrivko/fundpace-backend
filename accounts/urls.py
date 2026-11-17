from django.urls import path
from .views import AccountsHomeView #RegisterView, LoginView,

urlpatterns = [
    # Resulting URL: /api/v1/accounts/
    path("accounts/", AccountsHomeView.as_view(), name="accounts-home"),
    # path("accounts/register/", RegisterView.as_view(), name="register"),
    # path("accounts/login/", LoginView.as_view(), name="login"),
]