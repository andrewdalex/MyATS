from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.
def home(request,student_id):
    if student_id.isdigit():
        student_id = int(student_id)
    else:
        raise Http404('Not a Valid Id')
    student = get_object_or_404(Student, student_id = student_id)
    grade = student.student_grade
    if grade <=5:
        files = Resource.objects.filter(fourth_fifth=True)
    else:
        files = Resource.objects.filter(sixth_ninth=True)

    context = { 'files':files, 'student_id':student_id }
    return render(request,'home.html', context=context)


def SearchIdView(request):
    if request.method == "POST":
        form = SearchIdForm(request.POST)
        if form.is_valid():
            person_id = form.cleaned_data.get('person_id')
            student = get_object_or_404(Student, student_id=person_id)
            return redirect('home', student)
    else:
        form = SearchIdForm()
    return render(request, 'login.html', {"Search_Form": form})

def infoView(request, student_id, page_title):
    if student_id.isdigit():
        student_id = int(student_id)
    else:
        raise Http404('Not a Valid Id')
    student = get_object_or_404(Student, student_id=student_id)
    resource = get_object_or_404(Resource, resource_name=page_title)
    context = {'resource':resource, 'student':student}
    return render(request, 'infoPage.html', context=context)
