from django.db import models
from django.conf import settings



class Tag(models.Model):
    class Meta:
        db_table = "tag"

    tag = models.CharField(max_length=256, default='')

    def __str__(self):
        return self.tag



class Movie(models.Model):
    class Meta:
        db_table = "movie"

    movieId = models.CharField(max_length=50)
    title = models.CharField(max_length=256, default='')
    image = models.URLField(max_length=256)
    score = models.DecimalField(max_digits=2, decimal_places=1)
    desc = models.TextField()
    tag = models.ManyToManyField(Tag, related_name='movies')

    def __str__(self):
        return self.title



class Taste(models.Model):
    class Meta:
        db_table = "taste"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    taste = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)