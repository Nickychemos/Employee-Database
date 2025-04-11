"""
URL configuration for EmployeeDB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from Employees.views import employee_list, employee_details, manager_list,\
manager_details, branch_list, branch_details, Kisumu_list, Nairobi_list, Mombasa_list
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/employees/', employee_list),
    path('api/employees/<int:id>', employee_details),
    path('api/managers/', manager_list),
    path('api/managers/<int:id>', manager_details),
    path('api/branches/', branch_list),
    path('api/branches/<int:id>', branch_details),
    path('api/<str:branch>', Kisumu_list),
    path('api/<str:branch>', Nairobi_list),
    path('api/<str:branch>', Mombasa_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)