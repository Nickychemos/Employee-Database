from django.contrib import admin
from .models import Employee, Branch, Manager

# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'employment_date', 'employee_code', 'manager', 'branch')
    search_fields = ['first_name', 'last_name']
    ordering = ['-employment_date']


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['branch_name']
    search_fields = ['branch_name']