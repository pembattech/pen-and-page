from django.urls import path, include
from .views import *

urlpatterns = [
    path("", home, name  = "home"),
    path("addblog/", add_blog, name = "addblog"),
    path("login/", login_view, name = "login" ),
    path("register/", register_view, name = "register" ),
    path("logout/", logout_view, name = "logout" ),
    path("blog_detail/<slug>", blog_detail, name = "blog_detail" ),
    path("blog_category/<category>", blog_category, name = "blog_category" ),
    path("profile/<int:authorid>", author_profile, name = "profile"),
    path("delete_blog/<id>", delete_blog, name = "delete_blog"),
    path("edit_blog/<slug>", edit_blog, name = "edit_blog"),
]

