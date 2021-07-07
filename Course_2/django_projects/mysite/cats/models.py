from os import name
from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Breed(models.Model):
    name = models.CharField(
        max_length=200,
        help_text= 'Enter a breed (e.g. Siamese)',
        validators= [MinLengthValidator(2, message='Make must be greater than 1 character')]
    )

    def __str__(self):
        return self.name

class Cat(models.Model):
    nickname = models.CharField(
        max_length=200,
        help_text= 'Enter a Cat Name (e.g. Pickles)',
        validators= [MinLengthValidator(2, message='Nickname must be greater than 1 character')]
    )
    weight = models.PositiveIntegerField()
    foods = models.CharField(max_length=500)
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nickname
    
