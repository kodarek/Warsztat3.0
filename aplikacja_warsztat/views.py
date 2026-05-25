from django.shortcuts import render

# Create your views here.
def awarie(request):
    return render(request, 'aplikacja_warsztat/awarie.html', {})