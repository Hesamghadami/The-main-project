from django import forms
from .models import *


class PostForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = ['title', 'content', 'image1', 'image2', 'image3', 'client','client_url', 'category', 'published_date']