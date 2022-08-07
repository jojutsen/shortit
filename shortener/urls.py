from django.contrib import admin
from django.urls import path
from shortener.views import  home, direct_url

urlpatterns = [
    path('',home,name='home'),
    path('<str:uid>', direct_url, name='direct')
]