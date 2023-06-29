from django.conf.urls import include
from django.urls import path
from django.urls import re_path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('board', views.board, name="home"),
    path('board_write', views.board_write, name="board_write"),
    path('board_insert', views.board_insert, name="board_insert"),
    path('board_view', views.board_view, name="board_view"),
    path('board_edit', views.board_edit, name="board_edit"),
    path('board_update', views.board_update, name="board_update"),
    path('board_delete', views.board_delete, name="board_delete"),

    
]
