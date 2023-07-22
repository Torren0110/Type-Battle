from django.db import models
from racer.models import Passage
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from django.utils import timezone

def getStartTime():
    return timezone.now() + timezone.timedelta(seconds=10)

# Create your models here.

class Lobby(models.Model):
    playerCount = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5, message="There can only be 5 player at max in a lobby.")])
    passage = models.ForeignKey(Passage, on_delete=models.CASCADE)
    difficulty = models.PositiveIntegerField(validators=[MaxValueValidator(2, message="Difficulty can not be more than 2")])
    startTime = models.DateTimeField(default=getStartTime)


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lobby = models.ForeignKey(Lobby, on_delete=models.SET_NULL, blank=True, default= None, null=True)

    def __str__(self):
        return self.user.username
    
class PlayerProgress(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    lobby = models.ForeignKey(Lobby, on_delete=models.CASCADE)
    wpm = models.PositiveIntegerField(default=0)
    progress = models.PositiveIntegerField(default=0)
    accuracy = models.PositiveIntegerField(default=100)

    def __str__(self):
        return self.player.user.username
