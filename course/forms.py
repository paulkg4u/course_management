from django import forms
from .models import Course

class CourseForm(forms.ModelForm):

    class Meta:
         model = User
         fields = '__all__'