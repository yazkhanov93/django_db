from rest_framework import serializers
from account.models import User, UserProfile, CompanyProfile, Region
from rest_framework_simplejwt.tokens import RefreshToken


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    isAdmin = serializers.SerializerMethodField(read_only=True)
    isStaff = serializers.SerializerMethodField("get_isStaff")

    class Meta:
        model = User
        fields = ["id", "email", "isAdmin", "is_staff"]

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_isStaff(self, obj):
        return self.is_staff


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ["id", "isAdmin", "token", "is_staff"]

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class CompanyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = '__all__'