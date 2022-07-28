from rest_framework import serializers
from account.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    is_admin = serializers.SerializerMethodField(read_only=True)
    is_staff = serializers.SerializerMethodField("get_isStaff")

    class Meta:
        model = User
        fields = ["id", "name", "surname","email", "isAdmin", "isStaff"]

        def get_isAdmin(self, obj):
            return obj.is_staff

        def get_isStaff(self, obj):
            return self.is_staff


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ["id", "name", "surname", "isAdmin", "token", "is_staff"]

        def get_token(self, obj):
            token = ResfreshToken.for_user(obj)
            return str(token.access_token)