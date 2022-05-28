from .models import mdl_events
from django.shortcuts import render
from django.contrib import auth


def index(request):
    # mdl_events.objects.filter(action='created')
    # mdl_changes = mdl_events.objects.valies_list('id', 'eventname', 'other', 'courseid', 'timecreated')
    # этот метод предпочтительнее ниже используемого так как мы не вскрываем стороннему пользователю структуру нашей БД.
    # Это определенно надо исправить, нно для тестовый версии подходит и так
    mdl_changes = mdl_events.objects.all()
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
    return render(request, 'moodle_events/help.html')


def testers(request):
    args = {'username': auth.get_user(request).username, 'emplname': auth.get_user_model()}
    return render(request, 'moodle_events/mdl-events.html', args)
