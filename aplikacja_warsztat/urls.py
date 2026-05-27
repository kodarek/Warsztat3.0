from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.awarie, name='awarie'),
    path('awarie/new/', views.awarie_new, name='awarie_new'),
]