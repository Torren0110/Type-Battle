from racer.models import Passage
import random

difficulties = [
    'easy',
    'medium',
    'hard',
    'god mode'
]

def checkDifficulty(diff):
    diff = diff.lower()
    if(diff in difficulties):
        return True
    return False

def getPassage(diff):
    diff = diff.lower()

    difficulty = difficulties.index(diff)

    text = Passage.objects.filter(difficulty = difficulty)

    if(not text.exists()):
        return ""
    
    maxInd = text.count() - 1

    index = random.randint(0, maxInd)

    text = text[index]

    return text.text
