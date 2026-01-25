from django import forms
from .models import Post

# posts/forms.py
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'photo', 'category'] # Add category here