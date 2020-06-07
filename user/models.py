from ckeditor.widgets import CKEditorWidget
from django.db import models
#forms notform
# Create your models here.
from django.forms import ModelForm, Select, TextInput, FileInput

from post.models import Post, Category, Images


class PostForm(ModelForm):
    class Meta:
        model =Post
        fields = ['category', 'title', 'keyword', 'description', 'image', 'detail', 'slug']
        widgets = {
            'category': Select(attrs={'class': 'comment_input', 'placeholder': 'category'}, choices=Category.objects.all()),
            'title': TextInput(attrs={'class': 'comment_input', 'placeholder': 'title'}),
            'keyword': TextInput(attrs={'class': 'comment_input', 'placeholder': 'keywords'}),
            'description': TextInput(attrs={'class': 'comment_input', 'placeholder': 'description'}),
            'image': FileInput(attrs={'class': 'fileinput', 'placeholder': 'image'}),
            'detail': CKEditorWidget(),
            'slug': TextInput(attrs={'class': 'comment_input', 'placeholder': 'slug'}),
        }


class PostImageForm(ModelForm):
    class Meta:
        model = Images
        fields = ['title', 'image']
