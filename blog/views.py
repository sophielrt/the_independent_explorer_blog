from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def the_independent_explorer_blog(request):
    return HttpResponse("Hello, blog!")