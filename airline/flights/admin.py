from django.contrib import admin

from .models import Flight, Airoport

# Register your models here.
admin.site.register(Airoport)
admin.site.register(Flight)
