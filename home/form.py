from django import forms
from .models import *


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'short_description', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            "short_description":  forms.Textarea(attrs={'placeholder': 'Enter short-description here', 'oninput': 'autoExpand(this)'}),
            'content': forms.Textarea(attrs={'placeholder': 'Enter content here', 'oninput': 'autoExpand(this)'}),
        }