from django.urls import path, include


from accounts.api.v1 import views

app_name = "api-v1"

urlpatterns = [
    path(
        "password-reset-link/",
        views.EmailPasswordReset.as_view(),
        name="password-reset-link",
    ),
    path(
        "password-reset-confirm/<str:token>/",
        views.PasswordResetConfirmView.as_view(),
        name="password-reset-confirm",
    ),
]
