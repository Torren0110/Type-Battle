from django.shortcuts import render, HttpResponse, redirect
from .util import checkDifficulty, getRoom, getText, getUserData, setUserData
from django.contrib import messages
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.

def menu(request):
    return render(request, 'multi/menu.html')

def battle(request, difficulty):
    if(checkDifficulty(difficulty)):
        room = getRoom(difficulty, request.user)
        text = getText(room)
        remTime = (room.startTime - timezone.now()).seconds

        context = {
            'battleText': text,
            'countDown': remTime
        }

        return render(request, 'multi/battle.html', context=context)
    
    messages.warning(request, "Select a Difficulty to Continue")

    return redirect('multi-menu')


def getInfo(request):
    if(request.method == "GET"):
        userData = getUserData(request.GET['userID'])

        data = {
            'data': userData
        }
        return JsonResponse(data)
    
    return JsonResponse({})

@csrf_exempt
def postInfo(request):
    if(request.method == "POST"):
        setUserData(request.POST)

    return HttpResponse("Success")