from django.db import models


# Create your models here.

class Award(models.Model):
    name = models.CharField(max_length=70)
    year = models.IntegerField()

    def __str__(self):
        return self.name


class Studio(models.Model):
    name = models.CharField(max_length=70)
    creation_date = models.DateField()
    place = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=70)
    birthdate = models.DateField()
    nationality = models.CharField(max_length=70)
    date_of_death = models.DateTimeField(blank=True)
    awards = models.ManyToManyField(Award)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=70)
    birthdate = models.DateField()
    nationality = models.CharField(max_length=70)
    date_of_death = models.DateTimeField(blank=True)
    height = models.IntegerField()
    awards = models.ManyToManyField(Award)
    biography = models.TextField()

    def __str__(self):
        return self.name


class Show(models.Model):
    title = models.CharField(max_length=80)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
    release_date = models.DateField()
    awards = models.ManyToManyField(Award)
    description = models.TextField()


class Movie(Show):
    def __str__(self):
        return self.title


class Series(Show):
    seasons_number = models.IntegerField()

    def __str__(self):
        return self.title


class Grade(models.Model):
    grade = models.IntegerField()
    date = models.DateField()
    user = models.CharField(max_length=50)
    movie = models.ForeignKey(Show, on_delete=models.CASCADE)

    def __str__(self):
        return self.grade


class Review(models.Model):
    review = models.TextField()
    date = models.DateField()
    user = models.CharField(max_length=50)
    movie = models.ForeignKey(Show, on_delete=models.CASCADE)

    def __str__(self):
        return self.review
