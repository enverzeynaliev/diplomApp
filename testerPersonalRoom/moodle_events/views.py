from django.http import HttpResponse

from .models import mdl_events
from django.shortcuts import render


def index(request):
    mdl_events.objects.filter(action='created')
    # mdl_changes = mdl_events.objects.valies_list('id', 'eventname', 'other', 'courseid', 'timecreated')
    # этот метод предпочтительнее ниже используемого так как мы не вскрываем стороннему пользователю структуру нашей БД.
    # Это определенно надо исправить, нно для тестовый версии подходит и так
    mdl_changes = mdl_events.objects.all()
    return render(request, 'moodle_events/mdl-events.html', {'mdl_changes': mdl_changes})


# WHERE(`action` = 'created'
# OR
# `action` = 'updated') AND(`target` = 'course_section'
# OR
# `target` = 'course_section'
# OR
# `target` = 'course');

def helppage(request):
    return HttpResponse("<h3>А тут мы сможем почитать, как работать с программой. Ну, а пока тут lorem...</h3>")


def custom_login(request):
    return render(request, 'mooodle_events/custom_login.html')
