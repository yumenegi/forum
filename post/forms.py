from django.forms import ModelForm, fields
from .models import Post, Profile
from django.contrib.auth.models import User

class SubmitPost(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
