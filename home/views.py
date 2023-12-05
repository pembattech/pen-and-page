from .models import Blog
from django.shortcuts import render, redirect
from django.contrib.auth import logout

from .form import *


def home(request):
    categories = Blog.objects.values_list('category', flat=True).distinct()
    context = {"categories": categories, "blogs": Blog.objects.all()}
    return render(request, 'home.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect("/")
    
    # if 'next' in request.POST:
    #     print("Hello1")
    
    #     return redirect(request.POST['next'])
    
    return render(request, 'login.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect("/")
    print(request)
    return render(request, 'register.html')


def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect("/")
