from django.contrib import admin

from .models import Post, Profile, Thread

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Thread)