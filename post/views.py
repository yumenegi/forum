from django.http.request import HttpRequest
from django.shortcuts import redirect, render
from django.template import loader
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import SubmitPost, RegisterForm
from .models import Post, Thread
import datetime

# Create your views here.

from django.http import HttpResponse

from .models import Post


def index(request):
    return render(request, 'post/landing.html')


def detail(request, post_id):
    # shows content of the post
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'post/detail.html', context)


class LogIn(View):
    def get(self, request):
        context = {}
        return render(request, 'post/logIn.html', context)

    def post(self, request):
        # if request.POST.has_key('username'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/all/')

        return HttpResponse('invalid')


class NewPost(View):
    def get(self, request):
        if request.user.is_anonymous:
            return HttpResponse('Please Sign In')

        form = SubmitPost()
        context = {'form': form}
        return render(request, 'post/newPost.html', context)

    def post(self, request):
        form = request.POST
        # print(thre)
        save_data = Post.objects.create(
            userPosted=request.user,
            thread=get_object_or_404(Thread, pk=form['thread']),
            title=form['title'],
            content=form['content'],
            pub_date=datetime.datetime.now(),
        )
        save_data.save()
        return HttpResponseRedirect('/posts/' + str(save_data.id))


class NewThread(View):
    def get(self, request):
        if request.user.is_anonymous:
            return HttpResponse('Please Sign In')
        return render(request, 'post/newThread.html')

    def post(self, request):
        form = request.POST
        save_data = Thread.objects.create(title=form['title'])
        save_data.save()
        return HttpResponseRedirect('/threads/' + str(save_data.id))


class MainPage(View):
    def post(self, request):
        if 'logout' in request.POST.keys():
            logout(request)
        else:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

        # post_objects = Post.objects.order_by('pub_date')
        # context = {'post_objects': post_objects}

        # return render(request, 'post/index.html', context)
        return HttpResponseRedirect(request.path)

    def get(self, request):
        post_objects = Post.objects.order_by('-pub_date')
        context = {'post_objects': post_objects}
        return render(request, 'post/index.html', context)


class Threads(View):
    def post(self, request):
        if 'logout' in request.POST.keys():
            logout(request)
        else:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

        # post_objects = Post.objects.order_by('pub_date')
        # context = {'post_objects': post_objects}

        # return render(request, 'post/index.html', context)
        return HttpResponseRedirect(request.path)

    def get(self, request):
        thread_object = Thread.objects.all()
        context = {'thread_object': thread_object}
        return render(request, 'post/thread.html', context)


class ThreadView(View):
    def post(self, request, thread_id):
        if 'logout' in request.POST.keys():
            logout(request)
        else:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

        # post_objects = Post.objects.order_by('pub_date')
        # context = {'post_objects': post_objects}

        # return render(request, 'post/index.html', context)
        return HttpResponseRedirect(request.path)

    def get(self, request, thread_id):
        # print(thread_id)
        request_thread = get_object_or_404(Thread, pk=thread_id)
        # print(type(request_thread))
        post_objects = Post.objects.filter(thread=request_thread).order_by('-pub_date')
        print(post_objects)
        context = {'post_objects': post_objects, 'title': request_thread.title}
        return render(request, 'post/threadList.html', context)


class Register(View):
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse('Invalid')

        return HttpResponseRedirect('/login/')

    def get(self, request):
        form = RegisterForm()
        context = {'form':form}
        return render(request, 'post/register.html', context)

class Profile(View):
    def post(self, request, user_id):
        if 'logout' in request.POST.keys():
            logout(request)
        else:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

        return HttpResponseRedirect(request.path)

    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        post = Post.objects.filter(userPosted=user).order_by('-pub_date')
        is_self = user == request.user
        print(is_self)
        context = {'post_objects': post, 'is_self':is_self}
        return render(request, 'post/profile.html', context)
        
class Delete(View):
    def post(self, request, post_id):
        delete_post = get_object_or_404(Post, pk=post_id)
        if 'delete' in request.POST.keys() and request.user == delete_post.userPosted:
            delete_post.delete()
            return HttpResponseRedirect('/profile/' + str(request.user.id))
        else:
            return HttpResponseRedirect('/profile/' + str(request.user.id))

    def get(self, request, post_id):
        delete_post = get_object_or_404(Post, pk=post_id)
        context = {'post':delete_post}
        return render(request, 'post/delete.html', context)
        
# user regist
# deletion
# styling
