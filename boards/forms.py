from django import forms
from .models import Topic,Post

class PostForm(forms.ModelForm):
    
    class Meta:
        
        model = Post
        fields = ['message',]