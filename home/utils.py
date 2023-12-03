from django.utils.text import slugify
import string
import random


# Function to generate a random string of length N
def generate_random_string(N):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    return res

# Function to generate a unique slug based on the given text
def generate_slug(text):
    new_slug = slugify(text)  # Convert the text to a slug using Django's slugify function

    from home.models import Blog     
    # Check if a blog post with the same slug already exists
    if Blog.objects.filter(slug=new_slug).first():
        # If it exists, append a random string to the text and recursively generate a new slug
        return generate_slug(text + generate_random_string(5))
    
    # If the slug is unique, return it
    return new_slug
