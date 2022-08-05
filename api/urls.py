from django.urls import path, include

urlpatterns = [
    path("user/", include("api.authorization.urls")),
    path("vacancy/", include("api.vacancy.urls")),
    path("applicants/", include("api.applicants.urls")),
]