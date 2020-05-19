from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from post.models import Category


def index(request):
    return HttpResponse('Post Page')
