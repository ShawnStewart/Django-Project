from django.urls import path
from . import views

urlpatterns = [
    path('test', views.test, name='blog-test'),
    path('', views.home, name='blog-home'),
    path('about', views.about, name='blog-about'),
]
