from django.shortcuts import render, redirect
from guest_user.decorators import allow_guest_user
from django.contrib.auth.decorators import login_required
from .forms import AddPassageForm
from django.contrib import messages

# Create your views here.

@allow_guest_user
def home(request):
    return render(request, 'racer/home.html')

@login_required
def addPassage(request):
    if(not request.user.is_superuser):
        return redirect('home')
    
    if(request.method == "POST"):
        addForm = AddPassageForm(request.POST)

        if(addForm.is_valid()):
            addForm.save()
            messages.success(request, "Passage added successfully!!")
            return redirect('addPassage')

    else:
        addForm = AddPassageForm()
    

    context = {
        'form' : addForm
    }
    
    return render(request, 'racer/addPassage.html', context = context)
