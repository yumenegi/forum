import datetime

from django.db import models
from django.db.models.deletion import SET_NULL
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    bio = models.TextField(default="", blank=True)
    def __str__(self):
        return (str(self.user) + "'s profile")

class Thread(models.Model):
    title = models.TextField(max_length=100)

    def __str__(self):
        return self.title

class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    userPosted = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE,null=True, blank=True)
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return (str(self.id) + ': "' + self.title + '"' + " by " + str(self.userPosted))

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    
