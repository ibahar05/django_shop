from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path("login/",views.LoginView.as_view(),name="login"),
    # path("Register/",views.RegisterView.as_view(),name="register"),
    path("logout/",views.LogoutView.as_view(),name="logout"),
    # path("password-reset/",views.PasswordResetView.as_view(),name="password-reset"),
    path("api/v1/", include("accounts.api.v1.urls")),
]
