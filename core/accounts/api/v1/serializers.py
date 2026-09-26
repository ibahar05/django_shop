from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from accounts.models import User
from django.core import exceptions


class EmailPasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate(self, attrs):
        email = attrs.get("email")
        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({"detail": "user does not exist"})
        attrs["user"] = user_obj

        return attrs


class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password1 = serializers.CharField(required=True)
    new_password2 = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs.get("new_password1") != attrs.get("new_password2"):
            raise serializers.ValidationError({"detail": "passwords don't match"})
        try:
            validate_password(attrs.get("new_password1"))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"new password": list(e.messages)})

        return attrs
