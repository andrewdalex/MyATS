from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
# Create your models here.

class Parent(models.Model):
    parent_phone_number = models.CharField(max_length=20)
    parent_user = models.ForeignKey(User, unique=True)
    parent_address = models.CharField(max_length=150)
    parent_zipcode = models.CharField(max_length=5)
    parent_city = models.CharField(max_length=50)
    parent_state = models.CharField(max_length=25)
    class Meta:
        verbose_name_plural = 'Parents'
        verbose_name = 'Parent'
    def _get_full_name(self):
        return '{0}, {1}'.format(self.parent_user.last_name, self.parent_user.first_name)
    full_name = property(_get_full_name)
    def __str__(self):
        return self.full_name
class Student(models.Model):
    student_grade = models.SmallIntegerField()
    student_first_name = models.CharField(max_length=50)
    student_last_name = models.CharField(max_length=50)
    student_school = models.CharField(max_length=100)
    student_parent = models.ForeignKey(Parent, related_name='students')
    class Meta:
        verbose_name_plural = 'Students'
        verbose_name = 'Student'
    def __str__(self):
        return '{0}, {1}'.format(self.student_last_name, self.student_first_name)
class SummerClass(models.Model):
    students = models.ManyToManyField(Student, through='Enrollment')
    class_start = models.DateField()
    class_end = models.DateField()
    class_title = models.CharField(max_length=100)
    class_code = models.CharField(max_length=15)
    class_section = models.SmallIntegerField()
    class_location = models.CharField(max_length=20)
    class Meta:
        verbose_name_plural = 'Classes'
        verbose_name = 'Class'
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    summer_class = models.ForeignKey(SummerClass, on_delete=models.CASCADE)
    date_added = models.DateField()
    class Meta:
        verbose_name_plural = 'Enrollments'
        verbose_name = 'Enrollment'
