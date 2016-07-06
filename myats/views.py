from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from .forms import RegForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/login/')
def home(request):
    return HttpResponse('Home Page')
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
            return HttpResponseRedirect('/login/')
    else:
        form = RegForm()
    return render(request, 'createuser.html', {'form' : form})
