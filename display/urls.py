from django.urls import path
from . import views

app_name = 'display'
urlpatterns = [path("", views.display_home, name = "display")]

