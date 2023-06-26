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

def blog_detail(request, slug):
    context = {}
    try:
        blog_obj = Blog.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'blog_detail.html', context)

