from django.shortcuts import render
import requests
from .models import departments


# Create your views here.
# def departments():
#     return None


def menu():
    return None


def get_categories(request):
    all_departments = {}
    if 'name' in request.GET:
        name = request.GET['name']
        url = 'https://do.sevsu.ru/webservice/rest/server.php?wstoken=02c7e838953badad2b98ecdcbd7970f2&moodlewsrestformat=json&wsfunction=core_course_get_categories'
        response = requests.get(url)
        data = response.json()
        departments = data['departments']

        # https://do.sevsu.ru/webservice/rest/server.php?wstoken=02c7e838953badad2b98ecdcbd7970f2&wsfunction=core_course_get_courses_by_field&field=category&value=[что сюдда вставить?]&moodlewsrestformat=json
        for i in departments:
            departments_data = departments(
                id=i['#'],
                name=i['Название'],
                description=i['Описание'],
                descriptionformat=i['Формат описания'],
                parent=i['Родитель'],
                sortorder=i['Сортировка'],
                coursecount=i['Число курсов'],
                depth=i['Глубина'],
                path=i['Путь'],
            )
            departments_data.save()
            all_departments = departments.objects.all().order_by('-id')

    return render(request, 'meals/meal.html', {"all_departments": all_departments})


def departments_detail(request,departments=None):
    departments = departments.objects.get(id=id)
    print(departments)
    return render(request, 'adminpanel/departments.html', {'departments': departments})
