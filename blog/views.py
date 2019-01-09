from django.shortcuts import render
from django.http import HttpResponse


def test(request):
    return HttpResponse('<p>Test route working!</p>')


def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')
