from django.db import models
import uuid

# Create your models here.


class Manager(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        verbose_name_plural = 'Managers'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Branch(models.Model):
    branch_name = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        verbose_name_plural = 'Branches'

    def __str__(self):
        return self.branch_name



class Employee(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    employment_date = models.DateField()
    employee_code = models.UUIDField(default = uuid.uuid4, unique=True, editable=False)
    manager = models.ForeignKey('Manager', on_delete=models.CASCADE, related_name='employees')
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE, related_name='employees')


    class Meta:
        verbose_name_plural = 'Employees'
        

    def __str__(self):
        return f"Employee Name: {self.first_name} {self.last_name}"
    