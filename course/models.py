from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    max_credits = models.IntegerField(default=0)
    hours = models.IntegerField(default=0)

    def __str__(self):
        return self.name


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    subjects = models.ManyToManyField(Subject)
    course_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name + '-'+ self.course_type





