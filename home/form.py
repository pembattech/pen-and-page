from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import *

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ["title", "content", "category"]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'blogform-title', "label": "False", "placeholder": "New post title here..."}),
            'content': CKEditorWidget(),
            'cover_image': forms.ClearableFileInput(attrs={'class': 'blogform-fileupload input-file'}),
            'category': forms.Select(attrs={'class': 'blogform-category'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_content"]
        
        widgets = {
            'comment_content': forms.Textarea(attrs={'class': 'comment-input', "placeholder": "What are you thoughts?"}),
        }