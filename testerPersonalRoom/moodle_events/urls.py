from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.index),
    # Пока это отслеживается как стартовая страница, сайт запускается с этого. !!! надо обязательно исправить позже
    path('help',  views.helppage)
]
