from django.contrib import admin
from .models import Vacancy, JobType, JobCategory


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ["title", "salary", "jobType", "jobCategory", "region"]


@admin.register(JobType)
class JobTypeAdmin(admin.ModelAdmin):
    list_display = ["name",]


@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ["name",]