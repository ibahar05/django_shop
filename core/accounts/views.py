from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views
from django.views.generic import CreateView, View
from .models import User
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import redirect

from .forms import AuthenticationForms, CustomUserCreationForm


class LoginView(auth_views.LoginView):
    template_name = "accounts/login.html"
    form_class = AuthenticationForms
    redirect_authenticated_user = True


class LogoutView(View):
    def post(self, request):
        logout(request) 
        return redirect('accounts:login')


# class PasswordResetView(auth_views.PasswordResetView):
#     template_name = "accounts/password_reset_form.html"

class RegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("accounts:login")

