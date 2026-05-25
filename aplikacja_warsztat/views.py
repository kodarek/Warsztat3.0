from django.shortcuts import render
from .models import Awarie

# Create your views here.
def awarie(request):
    awaria = Awarie.objects.all()
    return render(request, 'aplikacja_warsztat/awarie.html', {})