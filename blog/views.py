from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Shawn',
        'title': 'Exploring Django!',
        'content': "Django is really neat!",
        'date_posted': 'January 9, 2019'
    },
    {
        'author': 'Mallorie',
        'title': 'My First Blog Post',
        'content': "Here is the blog content.",
        'date_posted': 'January 9, 2019'
    }
]


def test(request):
    return HttpResponse('<p>Test route working!</p>')


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
