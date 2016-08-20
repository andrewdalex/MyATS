from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
# Create your models here.

class Form(models.Model):
    form_name = models.CharField(max_length=150)
    form_deadline = models.DateField()
    class Meta:
        verbose_name = "Form"
        verbose_name_plural = "Forms"
    def __str__(self):
        return self.form_name

class Student(models.Model):
    student_user = models.OneToOneField(User, null=True)
    student_grade = models.SmallIntegerField()
    student_first_name = models.CharField(max_length=50)
    student_last_name = models.CharField(max_length=50)
    student_school = models.CharField(max_length=100)
    forms_received = models.ManyToManyField(Form, related_name='students_completed',through="ReceivedForm")
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
    def __str__(self):
        return self.class_title

class Resource(models.Model):
    upload = models.FileField()
    resource_name = models.CharField(max_length=150, null=True)
    class Meta:
        verbose_name = "PDF"
        verbose_name_plural = "PDFs"
    def __str__(self):
        return self.resource_name

class ReceivedForm(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_received = models.DateField()
    def __str__(self):
        return '{0},{1}'.format(self.student.student_last_name,self.student.student_first_name)
