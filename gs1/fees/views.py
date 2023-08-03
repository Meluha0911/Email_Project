from django.shortcuts import render

# Create your views here.
def python_fees(r):
    return render(r,'feesone.html')

def django_fees(r):
    return render(r,'feestwo.html')
