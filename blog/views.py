from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic
from .models import Post
from django.contrib.auth import authenticate, login, logout

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 4 # 4 posts per page = 2 rows of 2
    ordering = ["-published"]

def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    return render(request, "blog/post_detail.html", {"post": post},)

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "blog/admin_login.html", {"error": "Invalid credentials or not an admin."})
    return render(request, "blog/admin_login.html")

def admin_logout(request):
    logout(request)
    return redirect("admin_login")