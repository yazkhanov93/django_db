from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from vacancy.models import Vacancy, JobCategory, JobType
from .serializers import VacancySerializer, JobCategorySerializer, JobTypeSerializer


class VacancyView(APIView):
    """ Last Added Vacancy For Main Page """
    def get(self, request):
        # try:
        title = None
        jobtype = None
        jobcategory = None
        salary = None


        if request.query_params.get('title', None):
            title = request.query_params.get('title', None)
            vacancy = Vacancy.objects.filter(title__icontains=title)
            
        if request.query_params.get('type', None):
            jobtype = request.query_params.get('type', None)
            vacancy = Vacancy.objects.filter(jobType=jobtype)[:10]
        if request.query_params.get('category', None):
            jobcategory = request.query_params.get('category', None)
            vacancy = Vacancy.objects.filter(jobCategory=jobcategory)[:10]
        if request.query_params.get('salary', None):
            salary = request.query_params.get('salary', None)
            vacancy = Vacancy.objects.filter(salary=salary)[:10]
        else:
            vacancy = Vacancy.objects.all()[:10]
        serializer = VacancySerializer(vacancy, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # except:
        #     return Response({"detail":"No Vacancy"})


# class VacancyListView(APIView):
#     """ Vacancy List """
#     def get(self, request):
#         try:
#             jobtype = None
#             jobcategory = JobCategory.objects.all()
#             salary = None
#             if request.query_params.get('fulltime', None):
#                 jobtype = request.query_params.get('fulltime', None)
#                 vacancy = Vacancy.objects.filter(jobType=jobType)
#             else:
#                 vacancy = Vacancy.objects.all()
#             serializer = VacancySerializer(vacancy, many=True)
#             return Response(serializer.data)
#         except:
#             return Response({"detail":"No Vacancy"})
