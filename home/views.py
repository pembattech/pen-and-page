from django.shortcuts import render, redirect
from django.contrib.auth import logout 

from .form import *
from .models import CATEGORY_CHOICES

def home(request):
    categories = Blog.objects.values_list('category', flat=True).distinct()
    context = {"categories": categories, "blogs": Blog.objects.all()}
    return render(request, 'home.html', context)

def add_blog(request):
    context = {'form': BlogForm, 'category_choices': CATEGORY_CHOICES}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            image = request.FILES.get('file-upload-input', '')
            title = request.POST.get('title')
            user = request.user
            category = request.POST.get('category')
            
            if form.is_valid():
                print("test2")
                content = form.cleaned_data['content']
                short_description = form.cleaned_data['short_description']
                print("test3")
                print(user, title, short_description, content, category, image)
                
                blog_obj = Blog.objects.create(
                    author=user, title=title, short_description = short_description, 
                    content=content, category = category , image=image
                )
                print(blog_obj)
            return redirect('/addblog/')
    except Exception as e:
        print(e)
    
    return render(request, 'addblog.html', context)


def login_view(request):
    print(request)
    return render(request, 'login.html')

def register_view(request):
    print(request)
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

def blog_category(request, category):
    context = {}
    try:
        categories = Blog.objects.filter(category = category)

        context = {"ofcategory": categories}
    except Exception as e:
        print(e)
    
    return render(request, 'category_item.html', context)