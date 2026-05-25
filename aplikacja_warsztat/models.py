from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Awarie(models.Model):
     # Wybory dla pól z ograniczoną listą (dropdown)
    PRIORYTET_CHOICES = [
        ('niski', 'Niski'),
        ('sredni', 'Średni'),
        ('wysoki', 'Wysoki'),
        ('krytyczny', 'Krytyczny'),
    ]
    
    STATUS_CHOICES = [
        ('nowe', 'Nowe'),
        ('w_realizacji', 'W realizacji'),
        ('zamkniete', 'Zamknięte'),
    ]
    zglaszajacy = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_zgloszenia = models.DateTimeField(auto_now_add=True)
    lokalizacja = models.CharField(max_length=100)
    opis = models.TextField()
    priorytet = models.CharField(max_length=20, choices = PRIORYTET_CHOICES, default='średni')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='nowe' )
    uwagi_technika = models.TextField(blank=True, null=True, verbose_name='Uwagi')

    def __str__(self):
        return f"Zgłoszenie #{self.id} - {self.lokalizacja} ({self.status})"
    

    
    class Meta:
        verbose_name = "Awaria"
        verbose_name_plural = "Awarie"
