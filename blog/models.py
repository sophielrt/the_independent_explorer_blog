from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    read_time = models.IntegerField(help_text="Estimated read time in minutes")
    destination = models.CharField(max_length=200, help_text="Destination which the blog post is related to")
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(blank=True, null=True)
    view_count = models.IntegerField(default=0) # Need to edit this field to increment views automatically!

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.author}"