from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from .forms import RegForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.
@login_required
def home(request):
    u = request.user
    first_name = u.get_short_name()
    students = Student.objects.filter(student_parent=u.parent)
    context = { 'first_name':first_name, 'sudents':students }
    return render(request,'home.html', context=context)
def RegFormView(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('user_email')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username, email=email, password=password)
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()
            parent = Parent(parent_user = user)
            parent.save()
            return HttpResponseRedirect('/login/')
    else:
        form = RegForm()
    return render(request, 'createuser.html', {'form' : form})

@login_required
def ResourceView(request):
    files = Resource.objects.all()
    context = { 'files':files }
    return render(request, 'resources.html', context=context)
