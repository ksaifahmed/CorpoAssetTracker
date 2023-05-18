from django.urls import path
from .views import *

urlpatterns = [
    # Add new devices, names are assumed unique per company
    path('devices/add', DeviceCreateView.as_view(), name='device-create'),

    # List all devices for a company
    path('devices/list/', DeviceListView.as_view(), name='device-list'),
]
