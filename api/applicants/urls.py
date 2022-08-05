from django.urls import path
from . import views


urlpatterns = [
    path("applicant/", views.ApplicantView.as_view(), name="applicant"),
]