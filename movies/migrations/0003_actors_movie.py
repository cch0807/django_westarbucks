# Generated by Django 4.0.1 on 2022-01-11 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movies_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='actors',
            name='movie',
            field=models.ManyToManyField(through='movies.Actors_movies', to='movies.Movies'),
        ),
    ]
