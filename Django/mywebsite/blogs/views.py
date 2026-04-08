from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def home_page(request):
    return HttpResponse('<h1>Home page of our blogs<h1>')

def blogposts(request):
    return HttpResponse("All blog posts")

def python_intro(request):
    return HttpResponse("Python post")

def django_basic(request):
    return HttpResponse("Django basic blog post")

def python_oop(request):
    return HttpResponse("Python Object orientes programming")

def blog_post(request, blog):
    if blog == 'python_intro':
        res = 'Python Post'
    elif blog == "django-basic":
        res = "Django basic blog post"
    elif blog == 'python_oop':
        res = 'Python Object orientes programming'
    else :
        return HttpResponseNotFound("Blog Not found")
    return HttpResponse(res)

def blog_post_by_number(request, blog):
    return HttpResponse(blog)