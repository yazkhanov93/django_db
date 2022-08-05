from django.urls import path
from .import views

urlpatterns = [
    path("login/", views.MyTokenObtainPairView.as_view(), name="login"),
    path("user-register/", views.registerUser, name="user-register"),
    path("create-user-profile/", views.UserProfileView.as_view(), name="create-user-profile"),
    path("user-profile-list/", views.UserProfileView.as_view(), name="user-profile-list"),
    path("edit-user-profile/", views.UserProfileView.as_view(), name="edit-user-profile"),
    path("delete-user-profile/<int:pk>/", views.UserProfileDetail.as_view(), name="delete-user-profile"),

    path("create-company-profile/", views.CompanyProfileView.as_view(), name="create-company-profile"),
    path("company-profile-list/", views.CompanyProfileView.as_view(), name="company-profile-list"),
    path("edit-company-profile/<int:pk>/", views.CompanyProfileDetail.as_view(), name="edit-company-profile"),
    path("delete-company-profile/<int:pk>/", views.CompanyProfileDetail.as_view(), name="delete-company-profile"),
]