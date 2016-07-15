from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import User
# Create your models here.

class Parent(models.Model):
    parent_phone_number = models.CharField(max_length=20)
    parent_user = models.ForeignKey(User, unique=True)
    parent_address = models.CharField(max_length=150)
    parent_zipcode = models.CharField(max_length=5)
    parent_city = models.CharField(max_length=50)
    parent_state = models.CharField(max_length=25)
    
class Student(models.Model):
    student_grade = models.SmallIntegerField()
    student_first_name = models.CharField(max_length=50)
    student_last_name = models.CharField(max_length=50)
    student_school = models.CharField(max_length=100)
    student_parent = models.ForeignKey(Parent, related_name='students')

class Enrollment(model.Models):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    summer_class = models.ForeignKey(SummerClass, on_delete=models.CASCADE)
    date_added = models.DateField()
class SummerClass(models.Model):
    students = models.ManyToManyField(Student, through='Enrollment')
    class_start = models.DateField()
    class_end = models.DateField()
    class_title = models.CharField(max_length=100)
    class_code = models.CharField(max_length=15)
    class_section = models.SmallIntegerField()
    class_location = models.CharField(max_length=20)
