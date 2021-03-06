from django.views.generic import ListView
from django.contrib import auth
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import departments
from .models import course_on_categories
import requests


# Create your views here.
def menu():
    return None


def get_categories(request):
    all_departments = {}
    if 'name' in request.GET:
        name = request.GET['name']
        url = 'https://do.sevsu.ru/webservice/rest/server.php?wstoken=02c7e838953badad2b98ecdcbd7970f2' \
              '&moodlewsrestformat=json&wsfunction=core_course_get_categories '
        response = requests.get(url)
        data = response.json()
        department = data['departments']

        for i in departments:
            departments_data = departments(
                id=i['id'],
                name=i['name'],
                description=i['description'],
                descriptionformat=i['descriptionformat'],
                parent=i['parent'],
                sortorder=i['sortorder'],
                coursecount=i['coursecount'],
                depth=i['depth'],
                path=i['path'],
            )
            departments_data.save()
    all_departments = departments.objects.filter(id__contains=11).order_by('name')
    return render(request, 'adminpanel/departments.html', {"all_departments": all_departments,
                                                           'username': auth.get_user(request).username})


def menu(request):
    return request('/')


def get_courses_on_categories(request):
    all_category = {}

    # if 'categoryid' in request.GET:
    #     categoryid = request.GET['categoryid']
    url = 'https://do.sevsu.ru/webservice/rest/server.php?wstoken=02c7e838953badad2b98ecdcbd7970f2&wsfunction' \
          '=core_course_get_courses_by_field&field=category&value=9&moodlewsrestformat=json'
    response = requests.get(url)
    data = response.json()
    courses = data['courses']

    for i in courses:
        category_data = course_on_categories(
            id=i['id'],
            fullname=i['fullname'],
            displayname=i['displayname'],
            shortname=i['shortname'],
            categoryid=i['categoryid'],
            categoryname=i['categoryname']
        )
        category_data.save()
        # all_categories = course_on_categories.objects.filter(categoryid=request.GET['categoryid'])
        all_category = course_on_categories.objects.filter(categoryid=67)

    return render(request, 'adminpanel/course_on_categories.html',
                  {"all_category": all_category, 'username': auth.get_user(request).username})


def listing(request):
    course = course_on_categories.objects.all()
    paginator = Paginator(course, 5)  # Show 5 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'adminpanel/course_on_categories.html',
                  {"all_category": course, 'username': auth.get_user(request).username})
