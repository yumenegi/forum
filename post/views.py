from django.shortcuts import redirect, render
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .forms import SubmitPost
# Create your views here.

from django.http import HttpResponse

from .models import Post

def index(request):
    # temporary landing page
    return HttpResponse("<a href=\"/posts/\">posts here hi</a>")

def detail(request, post_id):
    # shows content of the post
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post' : post
    }
    return render(request, "post/detail.html", context)
    
def new_post(request):
    # create form
    form = SubmitPost()

    # if there is data coming in, normally GET, but when data, POST 
    if request.method == 'POST':
        print("POST!")
        form = SubmitPost(request.POST)
        if form.is_valid():
            save_data = form.save()
            return redirect("/posts/" + str(save_data.id) + "/")
    # print(form)
    context = {
        'form' : form
    }
    return render(request, 'post/newPost.html', context)

def post_list_view(request):
    post_objects = Post.objects.order_by("pub_date");
    context = {
        'post_objects' : post_objects
    }
    return render(request, "post/index.html", context)

