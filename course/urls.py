from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('', index, name = "index"),
    path('add_course', add_course, name = "add_course")
]