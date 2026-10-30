from django.db import models

# Create your models here.

from django.db import models


class Movie(models.Model):

    title = models.CharField(max_length=100)

    director = models.CharField(max_length=100)

    language = models.CharField(max_length=100)

    year = models.IntegerField()

    rating = models.FloatField()

    runtime = models.IntegerField()

    image = models.ImageField(
        upload_to='movies/',
        null=True,
        blank=True
    )


    def __str__(self):

        return self.title