from racer.models import Passage
import random
from django.utils import timezone
from .models import Lobby, PlayerProgress,Player


difficulties = [
    'easy',
    'medium',
    'hard'
]

def checkDifficulty(diff):
    diff = diff.lower()
    if(diff in difficulties):
        return True
    return False

def getRandomPassage(diff):
    diff = diff.lower()

    difficulty = difficulties.index(diff)

    text = Passage.objects.filter(difficulty = difficulty)

    if(not text.exists()):
        return None
    
    maxInd = text.count() - 1

    index = random.randint(0, maxInd)

    text = text[index]

    return text

def getRoom(diff, user):
    diff = diff.lower()
    difficulty = difficulties.index(diff)


    room = Lobby.objects.filter(difficulty=difficulty, playerCount__lt = 5, startTime__gt = timezone.now() + timezone.timedelta(seconds=3))
    player = Player.objects.get(user = user)

    if room.exists():
        room = room[0]
    else:
        room = Lobby(passage=getRandomPassage(diff), difficulty=difficulty)

    room.playerCount += 1
    playerProgress = PlayerProgress(player=player, lobby=room)
    player.lobby = room

    room.save()
    player.save()
    playerProgress.save()

    return room

def getText(room):
    return room.passage.text
    
def setUserData(data):
    progress = data['progress']
    WPM = data['WPM']
    accuracy = data['accuracy']
    player = Player.objects.get(user=data['userID'])
    lobby = player.lobby

    playerProgress = PlayerProgress.objects.get(lobby = lobby, player = player)
    playerProgress.wpm = WPM
    playerProgress.progress = progress
    playerProgress.accuracy = accuracy

    playerProgress.save()

def getUserData(userID):
    player = Player.objects.get(user=userID)
    lobby = player.lobby
    userDataDict = PlayerProgress.objects.filter(lobby=lobby)
    userData = []

    for ud in userDataDict:
        if(ud.player == player):
            continue

        userData.append({
            "userName": ud.player.user.username,
            "progress": f"{ud.progress} %",
            "WPM": ud.wpm
        })

    return userData



def getStartTime():
    return timezone.now() + timezone.timedelta(seconds=10)