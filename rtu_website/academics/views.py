from django.shortcuts import render
from academics.models import Branch, Year, Subjects, RtuPapers, Sub_Notes 

# Create your views here.

def home(request):
    dbba = Branch.objects.all()
    #dbba = dbba[1:]
    context = { "dbba":dbba }
    return render(request,'home.html', context)

def year(request, branch):
    context = { 'branch':branch }
    return render(request,'year.html', context)

def department(request, year, branch):
    context = { 'branch':branch, 'year':year }
    return render(request, 'department.html', context)

def subjects(request, branch, year, mod):
    dbba = Subjects.objects.filter(branch__name__contains=branch)
    dbbi = Subjects.objects.filter(year__year__contains=year)
    dbba = dbba.intersection(dbbi)
    context = { 'dbba':dbba, 'mod':mod }
    return render(request, 'subjects.html', context)

def multi(request, mod, subject):
    if(mod=='rtu'):
        dbba = RtuPapers.objects.filter(subject__subject__contains=subject)
        context = { 'dbba':dbba, 'subject':subject, 'heading':'RTU Papers' }
        return render(request,'multi.html', context)
    else:
        dbba = Sub_Notes.objects.filter(subject__subject__contains=subject)
        context = { 'dbba':dbba, 'subject':subject, 'heading':'Subject Notes' }
        return render(request,'multi.html', context)

#first year ko hold pr dalte h
def firstyear(request):
    context = { 'branch':'kuch', 'year':3 }
    return render(request, 'department.html', context)