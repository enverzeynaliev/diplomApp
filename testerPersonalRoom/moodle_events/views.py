
from django.contrib.auth.models import User

from .models import mdl_events
from django.shortcuts import render
from django.contrib import auth


def index(request):
    # mdl_events.objects.filter(action='created')
    mdl_changes = mdl_events.objects.all()
    # mdl_changes = mdl_events.objects.valies_list('id', 'eventname', 'other', 'courseid', 'timecreated')
    # этот метод предпочтительнее ниже используемого так как мы не вскрываем стороннему пользователю структуру нашей БД.
    # Это определенно надо исправить, нно для тестовый версии подходит и так

    return render(request, 'moodle_events/mdl-events.html',
                  {'mdl_changes': mdl_changes, 'username': auth.get_user(request).username})


# WHERE(`action` = 'created'
# OR
# `action` = 'updated') AND(`target` = 'course_section'
# OR
# `target` = 'course_section'
# OR
# `target` = 'course');

def helppage(request):
    return render(request, 'moodle_events/help.html', {'username': auth.get_user(request).username})


# def account_view(request):
#     user = User()
#     user_id = user.get_username()
#     items_in_cart = User.objects.filter(username=auth.get_user(request).username)
#     # если это суперпользователь
#     if request.user.is_superuser:
#         template = 'help.html'
#     # или если это просто пользователь с галочкой персонал
#     elif request.user.is_staff:
#         template = 'departments.html'
#     # или если это пользователь принадлежащий группе manager
#     elif request.user.groups.filter(name='manager').exists():
#         template = 'account_role.html'
#     # иначе все остальные (обычные пользователи)
#     else:
#         template = 'account.html'


