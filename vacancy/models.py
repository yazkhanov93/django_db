from django.db import models
from account.models import User, Region


class JobType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class JobCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jobCategory = models.ForeignKey(JobCategory, on_delete=models.SET_NULL, blank=True, null=True)
    jobType = models.ForeignKey(JobType, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    salary = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title