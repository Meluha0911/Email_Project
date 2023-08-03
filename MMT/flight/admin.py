from django.contrib import admin
from .models import Flight_Details

# Register your models here.
class Flight_Details_Admin(admin.ModelAdmin):
    list_display = ['fname','fdate','ffare','ffrom','fto']

admin.site.register(Flight_Details,Flight_Details_Admin)