from idlelib.multicall import r

from django.template.defaulttags import url
from django.urls import path, include, re_path
# from django.conf.urls import patterns, url
from . import views

urlpatterns = [
    path('', views.index),
    # Пока это отслеживается как стартовая страница, сайт запускается с этого. !!! надо обязательно исправить позже
    path('help', views.helppage)
    ]
