from django.urls import path
from .views import *

urlpatterns = [
    # Delegate devices to employees to employees of logged in company
    path('devices/delegate', DeviceDelegationCreateView.as_view(), name='device-delegation-create'),   

    # Get all device delegations of logged in company
    path('devices/delegations', DeviceDelegationsListView.as_view(), name='device-delegations-list'), 

    # Return a device delegated to an employee
    path('devices/return', DeviceDelegationRemoverView.as_view(), name='device-delegation-remover'),
]
