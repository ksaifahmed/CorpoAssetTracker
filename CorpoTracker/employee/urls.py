from django.urls import path
from .views import *

urlpatterns = [
    # Add new employees, names are assumed unique per company
    path('employees/add', EmployeeCreateView.as_view(), name='employee-create'),

    # List all employees for a company
    path('employees/list/', EmployeeListView.as_view(), name='employee-list'),
]