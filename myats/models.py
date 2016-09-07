from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
# Create your models here.


class Student(models.Model):
    #student_user = models.OneToOneField(User, null=True)
    person_grade = models.SmallIntegerField(verbose_name="Student's Grade")
    person_id = models.CharField(max_length=5, verbose_name="Student's ID#")
    class Meta:
        verbose_name_plural = 'People'
        verbose_name = 'Person'
    def __str__(self):
        return '{0}'.format(self.person_id)

class Resource(models.Model):
    upload = models.FileField()
    resource_name = models.CharField(max_length=150, null=True, verbose_name="Document Name")
    resource_description = models.TextField(verbose_name="Description")
    resource_alert_message = models.TextField(verbose_name="Alert Message", blank=True)
    fourth_fifth = models.BooleanField(verbose_name="4th-5th Program")
    sixth_ninth = models.BooleanField(verbose_name="6th-9th Program")
    teacher = models.BooleanField(verbose_name="Teacher")
    ta = models.BooleanField(verbose_name="TA")
    class Meta:
        verbose_name = "PDF"
        verbose_name_plural = "PDFs"
    def __str__(self):
        return self.resource_name
