from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Patron, Service
from .forms import MealSetForm


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    return render(request, 'home.html', {'Title': 'Home'})


############## PATRONS

@login_required
def patrons_index(request):
    patrons = Patron.objects.all()
    return render(request, 'patrons/index.html', {'Title': 'Patron Index', 'patrons': patrons})

@login_required
def patrons_detail(request, patron_id):
    patron = Patron.objects.get(id=patron_id)
    meal_form = MealSetForm()
    servicenull = Service.objects.exclude(id__in = patron.services.all().values_list('id'))
    return render(request, 'patrons/detail.html', {'Title': 'Patron Details', 'patron': patron, 'meal': meal_form, 'servicenull': servicenull })

@login_required
def add_mealset(request, patron_id):
    form = MealSetForm(request.POST)
    if form.is_valid():
        new_meal = form.save(commit=False)
        new_meal.patron_id = patron_id
        new_meal.save()
    return redirect('patron_detail', patron_id=patron_id)

@login_required
def services_index(request):
    services = Service.objects.all()
    return render(request, 'services/index.html', {'Title': 'Services Index', 'services': services })

@login_required
def services_detail(request, service_id):
    service = Service.objects.get(id=service_id)
    return render(request, 'services/detail.html', {'Title': 'Service Details', 'service': service })

def assoc_service(request, patron_id, service_id):
    Patron.objects.get(id=patron_id).services.add(service_id)
    return redirect('patron_detail', patron_id=patron_id)

def signup(request):
    form = UserCreationForm()
    error_message = ''

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('patrons_index')
        else:
            error_message = 'invalid cruedentials'
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
    

class PatronCreate(LoginRequiredMixin, CreateView):
    model = Patron
    fields = ('name', 'race', 'appearance', 'description')

class PatronUpdate(LoginRequiredMixin, UpdateView):
    model = Patron
    fields = '__all__'

class PatronDelete(LoginRequiredMixin, DeleteView):
    model = Patron
    success_url = '/patrons/'

class ServiceCreate(LoginRequiredMixin, CreateView):
    model = Service
    fields = '__all__'

class ServiceUpdate(LoginRequiredMixin, UpdateView):
    model = Service
    fields = '__all__'

class ServiceDelete(LoginRequiredMixin, DeleteView):
    model = Service
    success_url = '/services/'