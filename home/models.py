from django.db import models
from django.contrib.auth.models import User

from .utils import generate_slug

CATEGORY_CHOICES = (   
("Technology", "Technology"),
("Programming", "Programming"),
("Lifestyle", "Lifestyle"),
("Travel", "Travel"),
("Fashion", "Fashion"),
("Food", "Food"),
("Finance", "Finance")
)

class Blog(models.Model):
    title = models.CharField(max_length=1000)  # A field to store the title of the blog post.
    author = models.ForeignKey(User, on_delete=models.CASCADE, null= True)  # ForeignKey relationship with User model
    short_description = models.TextField(null=True)
    content = models.TextField()  # A field to store the main content of the blog post.
    slug = models.SlugField(max_length=1000, null=True, blank=True)  # A field to store a URL-friendly version of the title.
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, null = True)
    image = models.ImageField(upload_to="blog/")  # A field to store the image associated with the blog post.
    created_at = models.DateTimeField(auto_now_add=True)  # A field to store the timestamp when the blog post was created.
    upload_to = models.DateField(auto_now=True)  # A field to store the timestamp when the blog post was last updated.

    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Blog, self).save(*args, **kwargs)
