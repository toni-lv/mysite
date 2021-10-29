from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from bokeh.embed import server_document
from bokeh.settings import settings
settings.resources = 'inline'

# Create your views here.

def display_home(request: HttpRequest) -> HttpResponse:
    script = server_document('http://192.168.199.13:5500/app1')
    return render(request, 'display.html', {'script': script})
