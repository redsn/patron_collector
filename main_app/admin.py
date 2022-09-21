from django.contrib import admin

# Register your models here.

from .models import Patron

admin.site.register(Patron)