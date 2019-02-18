from django.db import models

class Director(models.Model):
    first_name = models.CharField(max_length = 15)
    last_name = models.CharField(max_length = 15)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name + self.last_name

class Movie(models.Model):
    director = models.ForeignKey(Director, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)

    def __str__(self):
        return self.title