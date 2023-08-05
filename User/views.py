from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import RegisterForm
from .models import User
from django.contrib.auth import authenticate , login
from django.contrib import messages

# Create your views here.


def base(request):
    return render(request , "base.html")

def login(request):
    if request.user.is_authenticated:
        return redirect('problem')

    if request.method == 'POST':
        username = request.POST.get("name")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('problem')
        else:
            messages.error(request, 'Username/Password is incorrect')

    return render(request, 'login.html')


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user=User(
                user_name=form.cleaned_data['user_name'],
                user_email=form.cleaned_data['user_email'],
                user_password=form.cleaned_data['user_password']
            )
            new_user.save()
            messages.success(request,'You are Registered, Now you can Login')
            return redirect('login')
        else:
            form = RegisterForm()
    return render(request , 'register.html' , {'forms' : form})