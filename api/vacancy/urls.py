from django.urls import path
from . import views


urlpatterns = [
    path("vacancy/", views.VacancyView.as_view(), name="vacancy"),
    path("vacancy-list/", views.VacancyListView.as_view(), name="vacancy-list"),
    path("vacancy-detail/<int:pk>/", views.VacancyDetailView.as_view(), name="vacancy-detail"),
]