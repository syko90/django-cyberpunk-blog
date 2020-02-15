from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def logowanie_widok(request):
    form = UserCreationForm()
    return render(request, 'konta/logowanie.html', {'form':form})