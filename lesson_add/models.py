from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50)


class Game(models.Model):
    name = models.CharField(max_length=100)
    genres = models.ManyToManyField("Genre", related_name='games')
    year_of_release = models.DateField()
    rating = models.DecimalField(decimal_places=2, max_digits=3)

