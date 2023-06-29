from django.conf.urls import include
from django.urls import path
from django.urls import re_path

from . import views

urlpatterns = [
    # path('', views.home, name="home"),
    path('album', views.album, name="home"),
    path('album_write', views.album_write, name="album_write"),
    path('album_insert', views.album_insert, name="album_insert"),
    path('album_view', views.album_view, name="album_view"),
    path('album_edit', views.album_edit, name="album_edit"),
    path('album_update', views.album_update, name="album_update"),
    path('album_delete', views.album_delete, name="album_delete"),

]
