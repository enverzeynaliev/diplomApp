from django.urls import path

from . import views

urlpatterns = [
    path('menu', views.menu),
    # эта страница должна быть начальной
    path('departments', views.departments)
]
