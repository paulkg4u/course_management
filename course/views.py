from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Subject, Course, TYPE_CHOICES

import json
# Create your views here.


def index(request):
    courses = Course.objects.all()
    return render(request,'index.html', {'name' : 'paul', 'courses' : courses})


def add_course(request):
    if request.method == 'GET':
        course_type_options = TYPE_CHOICES
        subjects = Subject.objects.all()
        return render(request, 'add_course.html', {'course' : 'add course', 'type_choices':TYPE_CHOICES, 'subjects' : subjects})
    elif request.method == 'POST':
        course_data = dict()
        course_data['name'] = request.POST.get('course_name')
        course_data['course_type'] = request.POST.get('course_type')
        new_course = Course.objects.create(**course_data)
        subjects = json.loads(request.POST.get('subjects',[]))
        for each_subject in subjects:
            id = each_subject.get('id', '')
            if id:
                subject = Subject.objects.get(id = int(id))
                new_course.subjects.add(subject)
            # subject = dict()

            # subject['name'] = each_subject.get('name', '')
            # subject['hours'] = each_subject.get('hours', '')
            # subject['max_credits'] = each_subject.get('max_credits', '')
            # new_subject = Subject.objects.create(**subject)
            # new_course.subjects.add(new_subject)
        return HttpResponseRedirect('/course')
        
    
