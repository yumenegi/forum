from django.shortcuts import render
from django.template import loader
from django.shortcuts import get_object_or_404, render

# Create your views here.

from django.http import HttpResponse

from .models import Post

def index(request):
    return HttpResponse("<a href=\"/posts/\">posts here hi</a>")

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post' : post
    }
    return render(request, "post/detail.html", context)
    

def post_list_view(request):
    post_objects = Post.objects.order_by("pub_date");
    context = {
        'post_objects' : post_objects
    }
    return render(request, "post/index.html", context)

