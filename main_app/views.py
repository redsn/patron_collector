from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Patron

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

class PatronCreate(CreateView):
    model = Patron
    fields = '__all__'

class PatronUpdate(UpdateView):
    model = Patron
    fields = '__all__'

class PatronDelete(DeleteView):
    model = Patron
    success_url = '/patrons/'