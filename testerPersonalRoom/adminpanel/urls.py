from django.urls import path

from . import views

urlpatterns = [
    path('menu', views.menu),
    # эта страница должна быть начальной
    path('departments', views.get_categories, name='id'),
    # path('/<int:id>/', views.departments_detail(), name='detail')
    path('category', views.get_courses_on_categories, name='categoryid')
]
