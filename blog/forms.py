from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'read_time', 'destination', 'featured_image', 'content', 'status', 'excerpt', 'published']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
            'excerpt': forms.Textarea(attrs={'rows': 3}),
            'published': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }