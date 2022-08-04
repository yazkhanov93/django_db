from django.contrib import admin
from .models import User, Region, UserProfile, CompanyProfile



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_superuser', 'is_active', 'is_staff']


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name',]


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname','birthday', 'phone']


@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'region', 'address']