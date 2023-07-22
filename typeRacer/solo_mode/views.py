from django.shortcuts import render, HttpResponse, redirect
from .util import checkDifficulty, getPassage
from django.contrib import messages

# Create your views here.

def menu(request):
    return render(request, 'solo/menu.html')

def battle(request, difficulty):
    if(checkDifficulty(difficulty)):
        text = getPassage(difficulty)
        
        context = {
            'battleText' : text
        }

        return render(request, 'solo/battle.html', context=context)
    else:
        messages.warning(request, "Select a Difficulty to Continue.")

    return redirect('solo-menu')