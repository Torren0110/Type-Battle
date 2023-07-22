from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from .utils import noInvalidSpaces
from django.utils import timezone

# Create your models here.

class Passage(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(validators=[noInvalidSpaces, MinLengthValidator(100, message='Passage must have atleast 100 charexters.')])
    difficulty = models.PositiveIntegerField(validators=[
        MaxValueValidator(3, message='Difficulty must be between 0 and 3.'),
        MinValueValidator(0, message='Difficulty must be between 0 and 3.')
    ])
    averageTime = models.DurationField(default=timezone.timedelta(0))
    totalTries = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title