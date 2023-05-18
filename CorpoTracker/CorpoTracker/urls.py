"""
URL configuration for CorpoTracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

# urls from apps
from company.urls import urlpatterns as company_urls
from employee.urls import urlpatterns as employee_urls
from device.urls import urlpatterns as device_urls
from devicelog.urls import urlpatterns as devicelog_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # company api urls
    path('api/', include(company_urls)),

    # employee api urls
    path('api/', include(employee_urls)),

    # device api urls
    path('api/', include(device_urls)),

    # devicelog api urls
    path('api/', include(devicelog_urls)),
]
