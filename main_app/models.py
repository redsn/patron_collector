from django.db import models
from django.urls import reverse

MEALSTART = (
    ('A', 'Mushroom Stew'),
    ('B', 'Fried Quail'),
    ('C', 'Garden Bits'),
    ('D', 'Chef\'s Choice')
)

MEALMID = (
    ('A', 'Bison Steak w/ SOTD'),
    ('B', 'Bison Roast w/ Potatoes'),
    ('C', 'Beet Salad w/ Goat Cheese')
)

MEALEND = (
    ('A', 'Mint Cake'),
    ('B', 'Butter Cookies')
)

# Create your models here.
class Patron(models.Model):
    name = models.CharField(max_length=16)
    race = models.CharField(max_length=30)
    appearance = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse('patrons_detail', kwargs={'patron_id': self.id})

class MealSet(models.Model):
    meal_start = models.CharField(
        max_length=1,
        choices=MEALSTART,
        default=MEALSTART[0][0]
    )