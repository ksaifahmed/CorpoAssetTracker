from django.db import models
from datetime import datetime
from django.apps import apps


# Create your models here.
class Employee(models.Model):
    employee_name = models.CharField(max_length=255)
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE)

    def devices(self):
        Device = apps.get_model('device', 'Device')
        return Device.objects.filter(employee=self)

    def check_out(self, device, condition):
        DeviceLog = apps.get_model('devicelog', 'DeviceLog')
        DeviceLog.objects.create(device=device, employee=self, condition=condition)

    def check_in(self, device):
        DeviceLog = apps.get_model('devicelog', 'DeviceLog')
        log = DeviceLog.objects.get(device=device, employee=self, return_at=None)
        log.return_at = datetime.now()
        log.save()