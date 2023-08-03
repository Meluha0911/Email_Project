from django.shortcuts import render
from rest_framework .views import APIView
from rest_framework .response import Response
from rest_framework import status
from .models import Flight_Details
from .serilizer import Flight_detials_Ser

# Create your views here.

class Flight(APIView):

    def get(self,r):
        flightdetails = Flight_Details.objects.all()
        serobj = Flight_detials_Ser(flightdetails,many=True)
        return Response(serobj.data)

    def post(self,r):
        serobj = Flight_detials_Ser(data = r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)
        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)
