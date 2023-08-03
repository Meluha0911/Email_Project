from django.shortcuts import render

# Create your views here.
def learn_python(r):
    return render(r,'course/courseone.html')

def learn_django(r):
    return render(r,'course/coursetwo.html')