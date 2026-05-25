from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.awarie, name='awarie')
]