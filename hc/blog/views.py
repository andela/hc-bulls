from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from hc.blog.forms import BlogCategoryForm,BlogPostForm

# Create your views here.
def all_blogs(request):
    return render(request, "blog/all_blogs.html")

@login_required
def new_blogs(request):
    blog=BlogPostForm()
    category=BlogCategoryForm()
    return render(request, "blog/new_blog.html",{"blog":blog,"category":category})    



