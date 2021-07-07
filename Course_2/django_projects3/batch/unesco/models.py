from django.db import models

# Create your models here.

class Category(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class State(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Region(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Iso(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Site(models.Model) :
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    justification = models.CharField(max_length=1024)
    year = models.IntegerField(null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    area_hectares = models.FloatField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


