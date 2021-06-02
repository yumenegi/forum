from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.http import HttpResponse
from .forms import SubmitPost, RegisterForm
from .models import Post, Thread
import datetime

# landing page
def index(request):
    # simply display a html page
    return render(request, 'post/landing.html')

# shows the details of the post
def detail(request, post_id):
    # request for the post data
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    # render the page with the specific post
    return render(request, 'post/detail.html', context)

# log in page
class LogIn(View):
    def get(self, request):
        # render log in page
        return render(request, 'post/logIn.html')

    def post(self, request):
        # get the username and password from query
        username = request.POST['username']
        password = request.POST['password']
        # authenticate the user
        user = authenticate(request, username=username, password=password)
        # if user authentication successful
        if user is not None:
            # log in user
            login(request, user)
            # redirects to front page
            return HttpResponseRedirect('/all/')

        # tells user that their log in is invalid, prompts user to try angain
        return HttpResponse('The log inforrmation is invalid, <a href="/login/">please try again</a>')

# new post creation
class NewPost(View):
    def get(self, request):
        # if no user signed in, ask user to sign in
        if request.user.is_anonymous:
            return HttpResponse('<a href="/login/">please sign in</a>')

        # if user is signed in
        # create form
        form = SubmitPost()
        context = {'form': form}
        # renders html with form
        return render(request, 'post/newPost.html', context)

    def post(self, request):
        # receive query dict with post data
        form = request.POST
        # creates the post object to be saved
        save_data = Post.objects.create(
            userPosted=request.user,
            thread=get_object_or_404(Thread, pk=form['thread']),
            title=form['title'],
            content=form['content'],
            pub_date=datetime.datetime.now(),
        )
        # save the new post
        save_data.save()
        # redirect user to the post they just created
        return HttpResponseRedirect('/posts/' + str(save_data.id))

# new thread creation page
class NewThread(View):
    def get(self, request):
        # user is not signed in, prompt them to sign in
        if request.user.is_anonymous:
            return HttpResponse('<a href="/login/">please sign in</a>')
        # if signed in, render page allowing them to post
        return render(request, 'post/newThread.html')

    def post(self, request):
        # receives form data and stores it
        form = request.POST
        # create new thread with received data
        save_data = Thread.objects.create(title=form['title'])
        # saves data
        save_data.save()
        # redirects user to their newly created thread
        return HttpResponseRedirect('/threads/' + str(save_data.id))

# index page, display all posts in database
class MainPage(View):
    def post(self, request):
        # user requested to log out
        if 'logout' in request.POST.keys():
            logout(request)
        # user requested to log in
        else:
            # gets username and password from form
            username = request.POST['username']
            password = request.POST['password']
            # authenticates user
            user = authenticate(request, username=username, password=password)
            # if authentication successful, logs user in
            if user is not None:
                login(request, user)
        # reload page
        return HttpResponseRedirect(request.path)

    def get(self, request):
        # get all posts and order by date latest first
        post_objects = Post.objects.order_by('-pub_date')
        # store posts in context and renders them
        context = {'post_objects': post_objects}
        return render(request, 'post/index.html', context)

# displays all available threads
class Threads(View):
    def post(self, request):
        # user requested to log out
        if 'logout' in request.POST.keys():
            logout(request)
        # user requested to log in
        else:
            # gets username and password from form
            username = request.POST['username']
            password = request.POST['password']
            # authenticates user
            user = authenticate(request, username=username, password=password)
            # if authentication successful, logs user in
            if user is not None:
                login(request, user)
        # reload page
        return HttpResponseRedirect(request.path)

    def get(self, request):
        # gets all threads
        thread_object = Thread.objects.all()
        # stores all threads in context and renders them
        context = {'thread_object': thread_object}
        return render(request, 'post/thread.html', context)

# display all posts in a specific thread
class ThreadView(View):
    def post(self, request, thread_id):
        # user requested to log out
        if 'logout' in request.POST.keys():
            logout(request)
        # user requested to log in
        else:
            # gets username and password from form
            username = request.POST['username']
            password = request.POST['password']
            # authenticates user
            user = authenticate(request, username=username, password=password)
            # if authentication successful, logs user in
            if user is not None:
                login(request, user)
        # reload page
        return HttpResponseRedirect(request.path)

    def get(self, request, thread_id):
        # gets the thread the page is displaying
        request_thread = get_object_or_404(Thread, pk=thread_id)
        # filters posts that are in the thread and stores them in context
        post_objects = Post.objects.filter(thread=request_thread).order_by('-pub_date')
        context = {'post_objects': post_objects, 'title': request_thread.title}
        # renders the specific thread with the posts of the thread
        return render(request, 'post/threadList.html', context)

# user registration page
class Register(View):
    def post(self, request):
        # gets the registration form
        form = RegisterForm(request.POST)
        # if the registration is valid
        if form.is_valid():
            form.save()
        # prompts user to try again
        else:
            return HttpResponse('<a href="/register/">Please try again</a>')
        # redirects user to log in
        return HttpResponseRedirect('/login/')

    def get(self, request):
        # gets the registration form
        form = RegisterForm()
        # stores form in context and renders it with crispy
        context = {'form':form}
        return render(request, 'post/register.html', context)

# user profile page
class Profile(View):
    def post(self, request, user_id):
        # user requested to log out
        if 'logout' in request.POST.keys():
            logout(request)
        # user requested to log in
        else:
            # gets username and password from form
            username = request.POST['username']
            password = request.POST['password']
            # authenticates user
            user = authenticate(request, username=username, password=password)
            # if authentication successful, logs user in
            if user is not None:
                login(request, user)
        # reload page
        return HttpResponseRedirect(request.path)

    def get(self, request, user_id):
        # gets the user of the profile
        user = get_object_or_404(User, pk=user_id)
        # gets the posts posted by this specific user and order them by date
        post = Post.objects.filter(userPosted=user).order_by('-pub_date')
        # if the user is the owner of the page, allows them to delete posts
        is_self = user == request.user
        # stores the user, flag and posts in context and renders them
        context = {'post_objects': post, 'is_self':is_self, 'profile_owner':user}
        return render(request, 'post/profile.html', context)

# deletion confirmaion page
class Delete(View):
    def post(self, request, post_id):
        # gets the post to be deleted
        delete_post = get_object_or_404(Post, pk=post_id)
        # if the user clicked the delete button indicated by the delete key
        if 'delete' in request.POST.keys() and request.user == delete_post.userPosted:
            # delete the post 
            delete_post.delete()
        # redirect user back to profile
        return HttpResponseRedirect('/profile/' + str(request.user.id))

    def get(self, request, post_id):
        # gets the post to be deleted
        delete_post = get_object_or_404(Post, pk=post_id)
        # stores it in context and renders
        context = {'post':delete_post}
        return render(request, 'post/delete.html', context)
