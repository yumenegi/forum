from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.MainPage.as_view()),
    path('posts/<int:post_id>/', views.detail, name='detail'),
    path('new/', views.NewPost.as_view(), name="new_post"),
    path('login/', views.LogIn.as_view(), name='login'),
]