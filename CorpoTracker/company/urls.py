from django.urls import path
from .views import *


urlpatterns = [
    path('register/', CompanyRegisterView.as_view(), name='company-register'),
    path('login/', CompanyLoginView.as_view(), name='company-login'),
    path('logout/', CompanyLogoutView.as_view(), name='company-logout'),
]
