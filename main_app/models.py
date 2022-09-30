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
class Service(models.Model):
    name = models.CharField(max_length=20)
    job = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.name}: {self.job}'

    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'service_id': self.id})

class Patron(models.Model):
    name = models.CharField(max_length=16)
    race = models.CharField(max_length=30)
    appearance = models.CharField(max_length=100)
    description = models.TextField()
    services = models.ManyToManyField(Service)

    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse('patron_detail', kwargs={'patron_id': self.id})

class MealSet(models.Model):
    mealstart = models.CharField(
        max_length=1,
        choices=MEALSTART,
        default=MEALSTART[0][0]
    )
    mealmid = models.CharField(
        max_length=1,
        choices=MEALMID,
        default=MEALMID[0][0]
    )
    mealend = models.CharField(
        max_length=1,
        choices=MEALEND,
        default=MEALEND[0][0]
    )
    patron = models.ForeignKey(Patron, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.patron.name}\'s meals'
