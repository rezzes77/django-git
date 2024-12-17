from django.contrib import admin
from .models import Clothes
from .models import Car

admin.site.register(Clothes)
admin.site.register(Car)