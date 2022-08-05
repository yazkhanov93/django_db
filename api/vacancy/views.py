from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from vacancy.models import Vacancy, JobCategory, JobType
from .serializers import VacancySerializer, JobCategorySerializer, JobTypeSerializer, VacancyDetailSerializer


class VacancyView(APIView):
    """ Last Added Vacancy For Main Page """
    def get(self, request):
        try:
            title = None
            jobtype = None
            jobcategory = None
            salary = None
            vacancy = Vacancy.objects.all()
            if request.query_params.get('title', None):
                title = request.query_params.get('title', None)
                vacancy = vacancy.filter(title__icontains=title)
            if request.query_params.get('type', None):
                jobtype = request.query_params.get('type', None)
                vacancy = vacancy.filter(jobType__name=jobtype)[:10]
            if request.query_params.get('category', None):
                jobcategory = request.query_params.get('category', None)
                vacancy = vacancy.filter(jobCategory__name=jobcategory)[:10]
            if request.query_params.get('salary', None):
                salary = request.query_params.get('salary', None)
                vacancy = vacancy.filter(salary=salary)[:10]
            else:
                vacancy = vacancy[:10]
            serializer = VacancySerializer(vacancy, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"detail":"No Vacancy"})

    def post(self, request):
        try:
            serializer = VacancySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except:
            return Response({"detail":"Please try again..."})
           

class VacancyListView(APIView):
    """ Vacancy List """
    def get(self, request):
        try:
            title = None
            region = None
            jobtype = None
            jobcategory = None
            salary = None
            vacancy = Vacancy.objects.all()
            if request.query_params.get('title', None):
                jobtype = request.query_params.get('title', None)
                vacancy = vacancy.filter(title=jobtype)
            if request.query_params.get('region', None):
                region = request.query_params.get('region', None)
                vacancy = vacancy.filter(region__name=region)
            if request.query_params.get('type', None):
                jobtype = request.query_params.get('type', None)
                vacancy = vacancy.filter(jobType__name=jobtype)
            if request.query_params.get('category', None):
                jobcategory = request.query_params.get('category', None)
                vacancy = vacancy.filter(jobCategory__name=jobcategory)
            if request.query_params.get('salary', None):
                salary = request.query_params.get('salary', None)
                vacancy = vacancy.filter(salary=salary)
            else:
                vacancy = vacancy
            serializer = VacancySerializer(vacancy, many=True)
            return Response(serializer.data)
        except:
            return Response({"detail":"No Vacancy"})


class VacancyDetailView(APIView):
    """ Vacancy Detail """
    def get(self, request, pk):
        try:
            vacancy = Vacancy.objects.get(id=pk)
            serializer = VacancyDetailSerializer(vacancy, many=False)
            return Response(serializer.data)
        except:
            return Response({"detail":"Vacancy does not exist"})

    def put(self, request, pk):
        try:
            vacancy = Vacancy.objects.get(id=pk)
            serializer = VacancyDetailSerializer(vacancy,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except:
            return Response({"detail":"Please try again"})

    def delete(self, request, pk):
        try:
            vacancy = Vacancy.objects.get(id=pk)
            vacancy.delete()
            return Response({"detail":"Vacancy was deleted"})
        except:
            return Response({"detail":"Please try again"})