# Generated by Django 2.1.5 on 2019-02-20 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
