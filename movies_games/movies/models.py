from django.db import models

class Movie(models.Model):
    movie_name = models.CharField(max_length = 100)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.movie_name

class Director(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 15, default = "Prakaj")
    last_name = models.CharField(max_length = 15, default = "Prakaj")
    age = models.IntegerField(default = 0)

    def __str__(self):
        return self.name