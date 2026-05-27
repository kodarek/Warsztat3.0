from django import forms
from .models import Awarie

class AwarieForm(forms.ModelForm):
    class Meta:
        model = Awarie
        fields = ('lokalizacja', 'opis', 'priorytet', 'status', 'uwagi_technika')