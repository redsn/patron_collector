from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Patron, Service
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
    meal_form = MealSetForm()
    return render(request, 'patrons/detail.html', {'Title': 'Patron Details', 'patron': patron, 'meal': meal_form })

def add_mealset(request, patron_id):
    form = MealSetForm(request.POST)
    if form.is_valid():
        new_meal = form.save(commit=False)
        new_meal.patron_id = patron_id
        new_meal.save()
    return redirect('patron_detail', patron_id=patron_id)

def services_index(request):
    services = Service.objects.all()
    return render(request, 'services/index.html', {'Title': 'Services Index', 'services': services })

def services_detail(request, service_id):
    service = Service.objects.get(id=service_id)
    return render(request, 'services/detail.html', {'Title': 'Service Details', 'service': service })


    

class PatronCreate(CreateView):
    model = Patron
    fields = '__all__'

class PatronUpdate(UpdateView):
    model = Patron
    fields = '__all__'

class PatronDelete(DeleteView):
    model = Patron
    success_url = '/patrons/'

class ServiceCreate(CreateView):
    model = Service
    fields = '__all__'

class ServiceUpdate(UpdateView):
    model = Service
    fields = '__all__'

class ServiceDelete(DeleteView):
    model = Service
    success_url = '/services/'