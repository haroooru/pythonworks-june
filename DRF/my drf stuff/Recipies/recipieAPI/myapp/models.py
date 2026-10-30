from django.db import models

# Create your models here.

from django.db import models

from django.db import models

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    meal_type = models.CharField(max_length=50)
    cuisine = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=100)
    instructions = models.CharField(max_length=100)
    image = models.ImageField()


