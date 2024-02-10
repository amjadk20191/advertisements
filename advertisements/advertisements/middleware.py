from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.exceptions import  InvalidToken
from django.utils.translation import gettext_lazy as _


class JWTAuthentication2(JWTAuthentication):

    def get_user(self, validated_token):

            try:
                user_id = validated_token[api_settings.USER_ID_CLAIM]
                user_group = validated_token['group']
            except KeyError:
                raise InvalidToken(_("Token contained no recognizable user identification"))


            return {"pk":user_id,"group":user_group}