from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Movie(models.Model):
    movie_name = models.CharField(max_length=50)
    movie_poster = models.ImageField(upload_to="images")
    movie_description = models.CharField(max_length=200,blank=True,null=True)
    users = models.ManyToManyField(User)

    def __str__(self) -> str:
        return self.movie_name
