from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.
@login_required
def home(request):
    u = request.user
    first_name = u.get_short_name()
    student = Student.objects.get(student_user=u)
    forms = Form.objects.order_by('form_deadline')
    received_forms = ReceivedForm.objects.filter(student=student)
    context = { 'first_name':first_name, 'forms':forms, 'student':student, 'received_forms':received_forms }
    return render(request,'home.html', context=context)

@login_required
def ResourceView(request):
    files = Resource.objects.all()
    context = { 'files':files }
    return render(request, 'resources.html', context=context)
