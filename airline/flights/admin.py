from django.contrib import admin

from .models import Flight, Airoport, Passenger

# Register your models here.
admin.site.register(Airoport)
admin.site.register(Flight)
admin.site.register(Passenger)
