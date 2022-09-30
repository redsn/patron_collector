from django.forms import ModelForm
from .models import MealSet

class MealSetForm(ModelForm):
    class Meta:
        model = MealSet
        fields = ('mealstart', 'mealmid', 'mealend')