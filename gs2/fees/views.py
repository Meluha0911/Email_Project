from django.shortcuts import render

# Create your views here.
def fees_python(r):
    return render(r,'fees/feesone.html')

def fees_django(r):
    return render(r,'fees/feestwo.html')