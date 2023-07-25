from django.shortcuts import render
from .models import *


def index(request):
    pages=Index.objects.all()
    context={
        'pages':pages
    }
    return render(request,'pages/index.html',context)

def map(request):
    return render(request, 'pages/harita.html')

def restaurant(request):
    pages=Restaurant.objects.all()
    context={
        'pages':pages
    }
    return render(request, 'pages/neyenir.html',context)

def beach(request):
    pages =Blog.objects.all()
    context={
        'pages':pages
    }
    return render(request, 'pages/PLAJLAR.html',context)

def hotel(request):
    pages=Hotel.objects.all()
    context={
        'pages':pages
    }
    return render(request, 'pages/konaklama.html',context)
