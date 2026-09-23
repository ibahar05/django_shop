from rest_framework.generics import GenericAPIView
from .serializers import EmailPasswordResetSerializer, PasswordResetConfirmSerializer
from mail_templated import EmailMessage
from ..utils import EmailThreading
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from .tokens import PasswordResetToken
from rest_framework_simplejwt.exceptions import TokenError
from accounts.models import User 

class EmailPasswordReset(GenericAPIView):
    """
    In this view user submit their email,
    if it is valida one time reset token will
    generate and email as a reset password link
    """

    serializer_class = EmailPasswordResetSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.validated_data["user"]
        token = self.get_token_for_users(user_obj)
        email_obj = EmailMessage(
            "email/passwordresetlink.tpl",
            {"token": token, "frontend_url": settings.FRONTEND_URL},
            settings.EMAIL_HOST_USER,
            to=[user_obj.email],
        )
        EmailThreading(email_obj).start()
        return Response(
            {"detail": "password reset link sent to your email"}, status=status.HTTP_201_CREATED
        )

    def get_token_for_users(self, user):
        token = PasswordResetToken.for_user(user)
        return str(token)



class PasswordResetConfirmView(GenericAPIView):
    """
    The user lands here after clicking the link in their email and submits
    a new password. The token is validated on several levels before the
    new password is accepted.
    """
    serializer_class = PasswordResetConfirmSerializer

    def post(self, request, token, *args, **kwargs):
        try:
            validated_token = PasswordResetToken(token)
        except TokenError:
            return Response(
                {"detail": "لینک نامعتبر یا منقضی شده است."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = User.objects.get(id=validated_token["user_id"])
        except User.DoesNotExist:
            return Response(
                {"detail": "کاربر یافت نشد."}, status=status.HTTP_400_BAD_REQUEST
            )

        if user.password[-10:] != validated_token.get("pwd_fragment"):
            return Response(
                {"detail": "لینک نامعتبر یا منقضی شده است."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user.set_password(serializer.validated_data["new_password1"])
        user.save()

        return Response(
            {"detail": "password changed successfully"},
            status=status.HTTP_200_OK,
        )