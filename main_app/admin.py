from django.contrib import admin

# Register your models here.

from .models import Patron, MealSet

admin.site.register(Patron),
admin.site.register(MealSet)