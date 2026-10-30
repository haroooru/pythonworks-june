# from django.db import models
#
# # Create your models here.
#
# from django.db import models


# Model Definition
# class Movie(models.Model):
#     title = models.CharField(max_length=30)
#     director = models.CharField(max_length=30)
#     language = models.CharField(max_length=30)
#     year = models.IntegerField()
#     rating = models.FloatField()
#     runtime = models.IntegerField()
#
#     def __str__(self):
#         return self.title

from django.db import models


# # Model Definition
# class Movie(models.Model):
#     title = models.CharField(max_length=30)
#     director = models.CharField(max_length=30)
#     language = models.CharField(max_length=30)
#     year = models.IntegerField()
#     rating = models.FloatField()
#     runtime = models.IntegerField()
#
#     # We'll add the image field before final migrations.
#     # image = models.ImageField(upload_to="movies", null=True, blank=True)


from django.db import models


# Model Definition
class Movie(models.Model):
    title = models.CharField(max_length=30)
    director = models.CharField(max_length=30)
    language = models.CharField(max_length=30)
    year = models.IntegerField()
    rating = models.FloatField()
    runtime = models.IntegerField()
    image = models.ImageField(
        upload_to="movies",
        null=True,
        blank=True
    )
