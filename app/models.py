from django.db import models


# Create your models here.

class User(models.Model):
    email = models.EmailField(max_length=100, primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    staff = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Award(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()

    def __str__(self):
        return self.name + ", " + str(self.year)


class Studio(models.Model):
    name = models.CharField(max_length=70)
    creation_date = models.DateField()
    ceo = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=70)
    birthdate = models.DateField()
    nationality = models.CharField(max_length=70)
    awards = models.ManyToManyField(Award, blank=True)
    image = models.FileField()

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=70)
    birthdate = models.DateField()
    nationality = models.CharField(max_length=70)
    height = models.IntegerField()
    awards = models.ManyToManyField(Award, blank=True)
    biography = models.TextField()
    image = models.FileField()

    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.CharField(max_length=80)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
    release_date = models.DateField()
    awards = models.ManyToManyField(Award, blank=True)
    description = models.TextField()
    image = models.FileField(blank=True)
    trailer = models.URLField()

    def __str__(self):
        return self.title


class Grade(models.Model):
    grade = models.IntegerField()
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.grade)


class Review(models.Model):
    review = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

    def __str__(self):
        return self.review
