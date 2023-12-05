from .models import Blog, Comment
from django.shortcuts import render, redirect
from django.contrib.auth import logout

from .form import *
from .models import CATEGORY_CHOICES


def home(request):
    categories = Blog.objects.values_list('category', flat=True).distinct()
    context = {"categories": categories, "blogs": Blog.objects.all()}
    return render(request, 'home.html', context)


def add_blog(request):
    if request.user.is_authenticated:
        context = {'form': BlogForm, 'category_choices': CATEGORY_CHOICES}
        try:
            if request.method == 'POST':
                form = BlogForm(request.POST)
                title = request.POST.get('title')
                print("test1")
                print(title)
                image = request.FILES.get('cover_image', '')
                print(image)
                user = request.user

                category = request.POST.get('category')
                print(category)
                if form.is_valid():
                    print("test2")
                    content = form.cleaned_data['content']

                    blog_obj = Blog.objects.create(
                        author=user, title=title, content=content, category=category, cover_image=image
                    )
                    print(blog_obj)
                return redirect('/new/')
        except Exception as e:
            print(e)

        return render(request, 'addblog.html', context)
    else:
        return render(request, 'login.html')


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


def blog_detail(request, slug):
    try:
        blog_obj = Blog.objects.filter(slug=slug).first()
        categories = Blog.objects.values_list('category', flat=True).distinct()

        if request.method == "POST":
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment_obj = comment_form.save(commit=False)
                comment_obj.author = request.user
                comment_obj.blog = blog_obj
                comment_obj.save()
                return redirect("blog_detail", slug=blog_obj.slug)
        else:
            comment_form = CommentForm()

        comment_count = Comment.objects.filter(blog=blog_obj).count()
        context = {
            "categories": categories,
            "blog_obj": blog_obj,
            "comment_form": comment_form,
            "comment_count": comment_count,
        }

    except Exception as e:
        print(e)
        context = {}

    return render(request, 'blog_detail.html', context)


def blog_category(request, category):
    context = {}
    try:
        categories = Blog.objects.filter(category=category)
        context = {"ofcategory": categories}
        categories = Blog.objects.values_list('category', flat=True).distinct()
        context["categories"] = categories
    except Exception as e:
        print(e)

    return render(request, 'category_item.html', context)


def author_profile(request, authorid):
    context = {}
    try:
        blog_obj = Blog.objects.filter(author_id=authorid)
        print(blog_obj)
        try:
            author = blog_obj.first().author
            print("*")
            print(blog_obj)
            print(author)
            print("*")
            context['blog_author'] = author
        except Exception as e:
            pass
        context['blog_obj'] = blog_obj
        context['logged_user'] = request.user
        print(context)

    except Exception as e:
        print(e)
    return render(request, 'author_profile.html', context)

def dashboard(request, authorid):
    context = {}
    try:
        blog_obj = Blog.objects.filter(author_id=authorid)
        print(blog_obj)
        try:
            author = blog_obj.first().author
            print("*")
            print(blog_obj)
            print(author)
            print("*")
            context['blog_author'] = author
        except Exception as e:
            pass
        context['blog_obj'] = blog_obj
        context['logged_user'] = request.user
        print(context)

    except Exception as e:
        print(e)
    return render(request, 'dashboard.html', context)

def delete_blog(request, id):
    try:
        blog_obj = Blog.objects.get(id=id)
        if blog_obj.author == request.user:
            blog_obj.delete()

    except Exception as e:
        print(e)

    return redirect("/")


def edit_blog(request, slug):
    context = {}
    try:
        blog_obj = Blog.objects.filter(slug=slug)
        if blog_obj.author != request.user:
            return redirect("/")

        initial_dict = {"content": blog_obj.content}
        form = Blog(initial=initial_dict)
        if request.method == "POST":
            form = BlogForm(request.POST)
            image = request.FILES.get('chooseFile', '')
            title = request.POST.get('title')
            user = request.user
            category = request.POST.get('category')

            if form.is_valid():
                print("test2")
                content = form.cleaned_data['content']

                blog_obj = Blog.objects.create(
                    author=user, title=title,
                    content=content, category=category, image=image
                )
                print(blog_obj)

                context['blog_obj'] = blog_obj
                context['form'] = form

    except Exception as e:
        print(e)

    return render(request, "edit_blog.html")
