from django.db import models
from django.apps import apps


# Create your models here.
class Device(models.Model):
    # name of device, unique for each company
    # serves as a unique identifier for each device
    device_name = models.CharField(max_length=255)

    # status of device--> new, used, broken
    # a choice field with 3 options
    STATUS_CHOICES = (
        ('new', 'new'),
        ('used', 'used'),
        ('broken', 'broken'),
    )

    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    # is the device currently in use by any employee?
    # newly added devices are not in use by default
    in_use = models.BooleanField(default=False)
    
    # the company that owns the device
    # whichever company account adds the device is the owner
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE)