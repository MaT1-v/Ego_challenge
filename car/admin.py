from django.contrib import admin

# Register your models here.
from .models import Car, Extra_info

admin.site.register(Car)
admin.site.register(Extra_info)