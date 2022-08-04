from rest_framework import serializers
from vacancy.models import Vacancy, JobCategory, JobType


class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = '__all__'


class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = '__all__'


class VacancySerializer(serializers.ModelSerializer):
    jobCategory = JobCategorySerializer()
    jobType = JobTypeSerializer()
    class Meta:
        model = Vacancy
        fields = ['title', 'user', 'jobType', 'jobCategory', 'description', 'region', 'salary', 'created', 'updated']