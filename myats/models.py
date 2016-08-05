from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    student_user = models.OneToOneField(User, null=True)
    student_grade = models.SmallIntegerField()
    student_first_name = models.CharField(max_length=50)
    student_last_name = models.CharField(max_length=50)
    student_school = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = 'Students'
        verbose_name = 'Student'
    def __str__(self):
        return '{0}, {1}'.format(self.student_last_name, self.student_first_name)
class Class(models.Model):
    students = models.ManyToManyField(Student)
    class_start = models.DateField()
    class_end = models.DateField()
    class_title = models.CharField(max_length=100)
    class_code = models.CharField(max_length=15)
    class_section = models.SmallIntegerField()
    class_location = models.CharField(max_length=20)
    class Meta:
        verbose_name_plural = 'Classes'
        verbose_name = 'Class'

class Resource(models.Model):
    upload = models.FileField()
