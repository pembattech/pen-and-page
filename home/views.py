from django.shortcuts import render, redirect
from django.contrib.auth import logout 

from .form import *

# Create your views here.


def home(request):
    context = {"blogs": Blog.objects.all()}
    return render(request, 'home.html', context)

def add_blog(request):
    return render(request, "addblog.html")

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect("/")

