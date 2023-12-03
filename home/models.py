from django.db import models
from django.contrib.auth.models import User

from ckeditor_uploader.fields import RichTextUploadingField

from .utils import generate_slug

CATEGORY_CHOICES = (
    ("Choose Category", "Choose Category"),
    ("Technology", "Technology"),
    ("Programming", "Programming"),
    ("Lifestyle", "Lifestyle"),
    ("Travel", "Travel"),
    ("Fashion", "Fashion"),
    ("Food", "Food"),
    ("Finance", "Finance"),
    ("Other", "Other")
)


class Blog(models.Model):
    # A field to store the title of the blog post.
    title = models.CharField(max_length=250)
    # ForeignKey relationship with User model
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = RichTextUploadingField(null=True)
    # A field to store a URL-friendly version of the title.
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    category = models.CharField(
        max_length=50, choices=CATEGORY_CHOICES, null=True, default="Choose Category")
    # A field to store the image associated with the blog post.
    cover_image = models.ImageField(upload_to="static/public/cover_image/")
    # A field to store the timestamp when the blog post was created.
    created_at = models.DateTimeField(auto_now_add=True)
    # A field to store the timestamp when the blog post was last updated.
    upload_to = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Blog, self).save(*args, **kwargs)
