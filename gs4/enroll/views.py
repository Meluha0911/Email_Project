from django.shortcuts import render
from .models import Student

# Create your views here.
def show(r):
    data = Student.objects.all()
    return render(r,'enroll/stddtl.html',{'stu':data})
