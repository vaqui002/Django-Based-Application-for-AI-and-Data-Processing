from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter post title', 'class': 'form-control'}),
            'content': forms.Textarea(attrs={'placeholder': 'Enter post content', 'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
