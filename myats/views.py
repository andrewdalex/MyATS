from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.
def home(request,person_id):
    person = get_object_or_404(Student, person_id = person_id)
    grade = person.person_grade
    if grade <=5:
        files = Resource.objects.filter(fourth_fifth=True)
    elif grade <=9:
        files = Resource.objects.filter(sixth_ninth=True)
    elif grade == 20:
        files = Resource.objects.filter(ta=True)
    else:
        files = Resource.objects.filter(teacher=True)
    context = { 'files':files, 'student_id': person_id }
    return render(request,'home.html', context=context)


def SearchIdView(request):
    if request.method == "POST":
        form = SearchIdForm(request.POST)
        if form.is_valid():
            person_id = form.cleaned_data.get('person_id')
            person = get_object_or_404(Student, person_id=person_id)
            return redirect('home', person_id)
    else:
        form = SearchIdForm()
    return render(request, 'login.html', {"Search_Form": form})
