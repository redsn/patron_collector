from django.db import models
from django.urls import reverse

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
