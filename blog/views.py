from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic
from .models import Post
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.text import slugify
from .forms import PostForm

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
            return redirect("admin_dashboard")
        else:
            return render(request, "blog/admin_login.html", {"error": "Invalid credentials or not an admin."})
    return render(request, "blog/admin_login.html")

def admin_logout(request):
    logout(request)
    return redirect("admin_login")

def is_staff(user):
    return user.is_staff

@login_required(login_url='/admin-login/')
@user_passes_test(is_staff, login_url='/admin-login/')
def dashboard(request):
    posts = Post.objects.all().order_by("-published")
    return render(request, "blog/admin_dashboard.html", {"posts": posts})

@login_required(login_url='/admin-login/')
@user_passes_test(is_staff, login_url='/admin-login/')
def post_add(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            post.save()
            return redirect("admin_dashboard")
    else:
        form = PostForm()
    return render(request, "blog/post_form.html", {"form": form, "action": "Add"})

@login_required(login_url='/admin-login/')
@user_passes_test(is_staff, login_url='/admin-login/')
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("admin_dashboard")
    else:
        form = PostForm(instance=post)
    return render(request, "blog/post_form.html", {"form": form, "action": "Edit"})

@login_required(login_url='/admin-login/')
@user_passes_test(is_staff, login_url='/admin-login/')
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("admin_dashboard")
    return render(request, "blog/post_delete.html", {"post": post})