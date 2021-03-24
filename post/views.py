from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.shortcuts import get_object_or_404, render


def index(request):
    return HttpResponse("posts here hi")

def detail(request, post_id):
    return HttpResponse(post_id)
    

