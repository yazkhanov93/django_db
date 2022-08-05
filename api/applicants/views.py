from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from applicants.models import Applicant
from .serializers import ApplicantSerializer


class ApplicantView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            applicants = Applicant.objects.all()
            serializer = ApplicantSerializer(applicants, many=True)
            return Response(serializer.data)
        except:
            return Response({"detail":"No applicants"})

    def post(self, request):
        data= request.data
        data["applicant_id"] = request.user.id
        serializer = ApplicantSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)
        return Response(serializer.data)