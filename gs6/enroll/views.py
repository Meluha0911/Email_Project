from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def showformdata(request):
  if request.method == 'POST':
     fm = StudentRegistration(request.POST)
     if fm.is_valid():
      print("form is valid")
      name = fm.cleaned_data['name']
      email = fm.cleaned_data['email']
      print('NAME:',name)
      print('EMAIL:',email)
      print(fm.cleaned_data['email'])
  else:
     fm = StudentRegistration()
     print("get request called")

  return render(request, 'enroll/userregistration.html', {'form':fm})
