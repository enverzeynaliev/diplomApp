from django.urls import path

from . import views

urlpatterns = [
    path('sign-in', views.login),
    # эта страница должна быть начальной
    path('sign-up', views.register),
    path('logout', views.logout)
]
