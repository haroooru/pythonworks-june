from django.db import models


# ============================================================
# EMPLOYEE MODEL
# ============================================================

# Model represents Employee table in database
class Employee(models.Model):

    # Employee ID must be unique
    # unique=True is used HERE in the MODEL
    empid = models.IntegerField(unique=True)

    # Employee name
    name = models.CharField(max_length=30)

    # Employee age
    age = models.IntegerField()

    # Employee place
    place = models.CharField(max_length=30)

    # Choices for gender
    # First value  -> database value
    # Second value -> display value
    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female')
    ]

    # Gender can only contain one of the above choices
    gender = models.CharField(
        max_length=20,
        choices=gender_choices
    )

    # Employee joining date
    joining_date = models.DateField()

    # Employee salary
    salary = models.IntegerField()

    # Employee job/designation
    designation = models.CharField(max_length=50)