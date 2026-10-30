
from django.db import models


class Department(models.Model):
    depname = models.CharField(max_length=100)
    depthead = models.CharField(max_length=100)

    def __str__(self):
        return self.depname


class Employee(models.Model):
    empid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
