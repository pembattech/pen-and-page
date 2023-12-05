from django import forms
from .models import *

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ["title", "content", "category"]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'blogform-title', "label": "False", "placeholder": "New post title here..."}),
            'content': forms.Textarea(attrs={'class': 'blogform-content'}),
            'cover_image': forms.ClearableFileInput(attrs={'class': 'blogform-fileupload input-file'}),
            'category': forms.Select(attrs={'class': 'blogform-category'}),
        }
