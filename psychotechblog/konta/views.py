from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def logowanie_widok(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # zaloguj użytkownika
            return redirect('wpisy:list')
    else:
        form = UserCreationForm()
    return render(request, 'konta/logowanie.html', {'form':form})