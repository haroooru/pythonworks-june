
from django.db import models

class Student(models.Model):
    roll_no = models.IntegerField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    place = models.CharField(max_length=100)
    marks = models.IntegerField()
