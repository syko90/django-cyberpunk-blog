from django.urls import path
from . import views

app_name ='konta'

urlpatterns = [
    path('logowanie/', views.logowanie_widok, name='logowanie'),
    
]