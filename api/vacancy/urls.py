from django.urls import path
from . import views


urlpatterns = [
    path("vacancy/", views.VacancyView.as_view(), name="vacancy"),
]