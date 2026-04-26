from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = 'blog/index.html'
    paginate_by = 4 # 4 posts per page = 2 rows of 2
    ordering = ["published"]
