from rest_framework import serializers
from .models import Flight_Details

class Flight_detials_Ser(serializers.ModelSerializer):
    class Meta:
        model = Flight_Details
        fields = "__all__"