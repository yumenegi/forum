from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.post_list_view),
    path('posts/<int:post_id>/', views.detail, name='detail'),
]