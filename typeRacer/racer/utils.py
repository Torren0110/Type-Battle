from django.core.exceptions import ValidationError

def noInvalidSpaces(text):
    if("  " in text):
        raise ValidationError("Passage cannot have consecutive spaces.")
    if(text[-1] == " "):
        raise ValidationError("Passage cannot end with a space.")
    
def checkEasy(str):
    for char in str:
        if(not (char.isalpha() or char == ' ' or char == ',' or char == '.')):
            return False
    return True

def checkMedium(str):
    if len(str) >= 200 or checkEasy(str):
        return False
    
    return True

def checkHard(str):
    if(len(str) < 200 or checkEasy(str)):
        return False
    
    return True
    
