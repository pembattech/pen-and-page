from django import forms
from .models import Blog
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'short_description', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'short_description': forms.Textarea(attrs={'placeholder': 'Provide a brief description here', 'oninput': 'autoExpand(this)'}),
            'content': forms.CharField(widget=CKEditorUploadingWidget()),
        }