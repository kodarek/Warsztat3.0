from django.shortcuts import render
from django.utils import timezone
from aplikacja_warsztat.models import Awarie
from .forms import AwarieForm 

# Create your views here.
def awarie(request):
    awaria = Awarie.objects.filter(data_zgloszenia__lte=timezone.now()).order_by('data_zgloszenia')
    
    return render(request, 'aplikacja_warsztat/awarie.html', {'awaria': awaria})

def awarie_new(request):
    form = AwarieForm()
    return render(request, 'aplikacja_warsztat/awarie_edit.html', {'form': form})