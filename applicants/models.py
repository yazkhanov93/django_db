from django.db import models
from account.models import User
from vacancy.models import Vacancy


class Applicant(models.Model):
    vacancy_id = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    applicant_id = models.ForeignKey(User, on_delete=models.CASCADE)
    received = models.BooleanField(default=False)
    refused = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.vacancy_id.title)