from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated

from account.models import User, UserProfile, CompanyProfile
from .serializers import UserSerializer, UserSerializerWithToken, UserProfileSerializer, CompanyProfileSerializer


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
            password=make_password(data["password"])
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        return Response({"detail":"This email already exist !!!"})


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            profile = UserProfile.objects.all()
            serializer = UserProfileSerializer(profile, many=True)
            return Response(serializer.data)
        except:
            return Response({"detail":"No Profiles"})

    def post(self, request):
        data = request.data
        data["user"] = request.user.id
        serializer = UserProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)
        return Response({"detail":"Profile created successfully"}) 

    def put(self, request):
        try:
            data= request.data
            serializer = UserProfileSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors)
            return Response(serializer.data)
        except:
            return Response({"detail":"Please try again..."})

class UserProfileDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        try:
            profile = UserProfile.objects.get(id=pk)
            serializer = UserProfileSerializer(profile, many=False)
            return Response(serializer.data)
        except:
            return Response({"detail":"Profile not found"})

    

    def delete(self, request, pk):
        profile = UserProfile.objects.get(id=pk)
        profile.delete()
        return Response({"detail":"Profile was deleted..."})


class CompanyProfileView(APIView):
    def get(self, request):
        try:
            profile =CompanyProfile.objects.all()
            serializer = CompanyProfileSerializer(profile, many=True)
            return Response(serializer.data)
        except:
            return Response({"detail":"No Profiles"})

    def post(self, request):
        serializer = CompanyProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)
        return Response({"detail":"Profile created successfully"})
       

class CompanyProfileDetail(APIView):
    def get(self, request, pk):
        try:
            profile = CompanyProfile.objects.get(id=pk)
            serializer = CompanyProfileSerializer(profile, many=False)
            return Response(serializer.data)
        except:
            return Response({"detail":"Profile not found"})

    def put(self, request, pk):
        try:
            profile = CompanyProfile.objects.get(id=pk)
            serializer = CompanyProfileSerializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except:
            return Response({"detail":"Please try again..."})

    def delete(self, request, pk):
        profile = CompanyProfile.objects.get(id=pk)
        profile.delete()
        return Response({"detail":"Profile was deleted..."})