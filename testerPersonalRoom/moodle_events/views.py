from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'moodle_events/mdl-events.html')


def helppage(request):
    return HttpResponse("<h3>А тут мы сможем почитать, как работать с программой. Ну, а пока тут lorem...</h3>")
