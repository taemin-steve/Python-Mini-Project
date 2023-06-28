from django.conf.urls import include
from django.urls import path
from django.urls import re_path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('board', views.board, name="home"),
]
