from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from account.models import User
from .serializers import UserSerializer, UserSerializerWithToken


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        try:
            data = super().validate(attrs)
            serializer = UserSerializerWithToken(self.user).data
            for k,v in serializer.items():
                data[k] = v
            return data
        except:
            raise ParseError({"detail":"Invalid email or password !!!"})


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(["POST"])
def registerUser(request):
    data = request.data
    try:
        user = User.objects.create(
            email=data["email"],
            name=data["name"],
            surname=data["surname"],
            password=make_password(data["password"])
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        return Response({"detail":"This email already exist !!!"})
