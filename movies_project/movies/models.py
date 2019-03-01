from django.db import models

class Celebrity(models.Model):
    first_name = models.CharField(max_length = 15)
    last_name = models.CharField(max_length = 15)
    age = models.IntegerField(default=0)
    typeof = models.CharField(max_length = 20)

    class Meta:
        verbose_name = ("Celebrity")
        verbose_name_plural = ("Celebrities")

    def __str__(self):
        return self.first_name + " " + self.last_name

class Movie(models.Model):
    celebrity = models.ForeignKey(Celebrity, on_delete = models.CASCADE, null = True)
    title = models.CharField(max_length = 100)
    description = models.TextField(null = True)
    genre = models.CharField(max_length = 50, null = True)
    rating = models.CharField(max_length = 10, null = True)

    def __str__(self):
        return self.title