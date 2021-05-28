from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.MainPage.as_view()),
    path('threads/', views.Threads.as_view()),
    path('posts/<int:post_id>/', views.detail, name='detail'),
    path('posts/<int:post_id>/delete', views.Delete.as_view(), name='delete'),
    path('threads/<str:thread_id>/', views.ThreadView.as_view(), name='threadview'),
    path('new/', views.NewPost.as_view(), name="new_post"),
    path('new/thread', views.NewThread.as_view(), name="new_post"),
    path('login/', views.LogIn.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('profile/<int:user_id>', views.Profile.as_view(), name='profile')
]