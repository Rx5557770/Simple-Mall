from typing import Any

from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.settings import api_settings

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    token_class = RefreshToken

    # 1.定制返回格式
    def validate(self, attrs: dict[str, Any]) -> dict[str, str]:
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        # 添加登录后业务状态码
        data['code'] = 200
        data['msg'] = 'success'
        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data

    # 2.定制荷载
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['email'] = user.email
        return token