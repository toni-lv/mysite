from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from bokeh.embed import server_document
from bokeh.settings import settings
settings.resources = 'inline'

# Create your views here.

def display_home(request: HttpRequest) -> HttpResponse:
    script = server_document(request.build_absolute_uri())
    return render(request, 'display.html', {'script': script})
