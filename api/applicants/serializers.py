from rest_framework import serializers
from applicants.models import Applicant
from api.vacancy.serializers import VacancyDetailSerializer



class ApplicantSerializer(serializers.ModelSerializer):
    # vacancy = VacancyDetailSerializer(many)
    class Meta:
        model = Applicant
        fields = '__all__'