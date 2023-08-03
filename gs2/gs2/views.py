from django.shortcuts import render


def home(r):
    return render(r,'home/home.html')