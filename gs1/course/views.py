from django.shortcuts import render

# Create your views here.
def learn_python(r):
    return render(r,'courseone.html',{'c':'python course'})

def learn_django(r):
        return render(r,'coursetwo.html')
