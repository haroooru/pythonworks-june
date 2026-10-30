from django.db import models


# Create your models here.
class Employee(models.Model):
    employee_id = models.IntegerField(unique=True)
    employee_name = models.CharField(max_length=100)
    employee_age = models.IntegerField()
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('Other', 'Other')
    ]
    employee_gender = models.CharField(max_length=20, choices=gender_choices)
    employee_salary = models.IntegerField()
    employee_joining_date = models.DateField()
    employee_designation = models.CharField(max_length=100)
    employee_image = models.ImageField(upload_to='employees',null=True)