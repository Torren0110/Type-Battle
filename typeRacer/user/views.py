from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


class MyLoginView(LoginView):
    def form_valid(self, form):
        messages.success(self.request, 'You are now logged in!!')
        return super().form_valid(form)

def log_out(request):
    logout(request)

    messages.success(request, "You have been logged out!!")

    return redirect('home')

def profile(request):
    return render(request, "user/profile.html")

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            messages.success(request, "Signup Successfull!!")
            return redirect('login')
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }

    return render(request, 'user/signup.html', context=context)


