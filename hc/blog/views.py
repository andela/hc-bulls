from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from hc.blog.forms import BlogCategoryForm,BlogPostForm
from django.shortcuts import redirect
from hc.blog.models import BlogCategory,BlogPost
from django.http import Http404, HttpResponse


# Create your views here.
def all_blogs(request):
    blogs=BlogPost.objects.all()

    return render(request, "blog/all_blogs.html",{"blogs":blogs})

@login_required
def new_blogs(request):
    current_user=request.user
    if request.method == "POST":
        blog_form=BlogPostForm(request.POST)
        if blog_form.is_valid():
            blog=blog_form.save(commit=False)
            blog.author=current_user
            blog.save()
            return redirect('hc-blogs')
    else:
        blog=BlogPostForm()   
    return render(request, "blog/new_blog.html",{"blog":blog})


def blog(request,blog_id):
    blog=BlogPost.objects.get(id=blog_id)
    return  render(request,"blog/single_blog.html",{"blog":blog})           

               



