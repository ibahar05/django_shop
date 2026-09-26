from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views

from .forms import AuthenticationForms


class LoginView(auth_views.LoginView):
    template_name = "accounts/login.html"
    form_class = AuthenticationForms
    redirect_authenticated_user = True


class LogoutView(auth_views.LogoutView):
    pass


# class PasswordResetView(auth_views.PasswordResetView):
#     template_name = "accounts/password_reset_form.html"
