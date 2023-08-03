from django.db import models

# Create your models here.
class Flight_Details(models.Model):
    fname = models.CharField(max_length=20)
    fdate = models.DateField()
    ffare = models.FloatField()
    ffrom = models.CharField(max_length=20)
    fto = models.CharField(max_length=20)

