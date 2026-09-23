from rest_framework_simplejwt.tokens import Token
from datetime import timedelta

class PasswordResetToken(Token):
    """ 
    This class generate reset token
    """
    token_type = "password reset"
    lifetime = timedelta(hours=48)

    @classmethod
    def for_user(cls, user):
        token = super().for_user(user)
        token["pwd_fragment"] = user.password[-10:]
        return token
    