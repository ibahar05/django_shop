from django.contrib.auth import forms as auth_forms
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User


class AuthenticationForms(auth_forms.AuthenticationForm):
    def confirm_login_allowed(self, user):
        super(AuthenticationForms, self).confirm_login_allowed(user)

        if not user.is_verified:
            raise ValidationError("user is not verified")


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("email",)

