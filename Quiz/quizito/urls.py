
from re import template
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('home/dashboard/', views.dashboard, name = 'dashboard'),
    path('home/questions/', views.question, name = 'question'),
    path('home/signup/', views.signup, name ='signup'),
    path('home/signin/', views.signin, name = 'signin'),
    path('home/signout/', views.signout, name = 'signout'),
]

