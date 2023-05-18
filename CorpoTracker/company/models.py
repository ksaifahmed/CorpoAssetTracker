from django.db import models
from django.apps import apps
from django.contrib.auth.models import User


# Create your models here.
class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)

    def employees(self):
        Employee = apps.get_model('employee', 'Employee')
        return Employee.objects.filter(company=self)

    def devices(self):
        Device = apps.get_model('device', 'Device')
        return Device.objects.filter(company=self)