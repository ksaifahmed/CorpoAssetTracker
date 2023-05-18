from django.db import models
from django.conf import settings

# Create your models here.
class DeviceLog(models.Model):
    # the device that is being checked out
    device = models.ForeignKey('device.Device', on_delete=models.CASCADE)

    # the employee that is checking out the device
    employee = models.ForeignKey('employee.Employee', on_delete=models.CASCADE)

    # the date and time the device was checked out
    check_out_at = models.DateTimeField(auto_now_add=True)

    # the date and time the device was returned
    return_at = models.DateTimeField(null=True, blank=True)

    # status of device--> new, used, broken
    # a choice field with 3 options
    STATUS_CHOICES = (
        ('new', 'new'),
        ('used', 'used'),
        ('broken', 'broken'),
    )

    # the status of the device when it was handed out
    condition = models.CharField(max_length=50, choices=STATUS_CHOICES)

    # the condition of the device when it was returned
    return_condition = models.CharField(max_length=50, null=True, blank=True, choices=STATUS_CHOICES)