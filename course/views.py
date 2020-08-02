from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Subject, Course
# Create your views here.


def index(request):
    courses = Course.objects.all()
    return render(request,'index.html', {'name' : 'paul', 'courses' : courses})


def add_course(request):
    if request.method == 'GET':
        return render(request, 'add_course.html', {'course' : 'add course'})
    elif request.method == 'POST':
        course_data = dict()
        course_data['name'] = request.POST.get('name')
        course_data['course_type'] = request.POST.get('course_type')
        new_course = Course.objects.create()
        return HttpResponseRedirect('/course')
        
    
