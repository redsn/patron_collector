from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Patron, MealSet
from .forms import MealSetForm

# Create your views here.
def home(request):
    return render(request, 'home.html', {'Title': 'Home'})


############## PATRONS

def patrons_index(request):
    patrons = Patron.objects.all()
    return render(request, 'patrons/index.html', {'Title': 'Patron Index', 'patrons': patrons})

def patrons_detail(request, patron_id):
    patron = Patron.objects.get(id=patron_id)
    return render(request, 'patrons/detail.html', {'Title': 'Patron Details', 'patron': patron})

def add_mealset(request, patron_id):
    form = MealSetForm(request.POST)
    if form.is_valid():
        new_meal = form.save(commit=False)
        new_meal.patron_id = patron_id
        new_meal.save()
    return redirect('patron_detail', patron_id=patron_id)

    

class PatronCreate(CreateView):
    model = Patron
    fields = '__all__'

class PatronUpdate(UpdateView):
    model = Patron
    fields = '__all__'

class PatronDelete(DeleteView):
    model = Patron
    success_url = '/patrons/'