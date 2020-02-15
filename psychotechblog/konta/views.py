from django.shortcuts import render

# Create your views here.
def logowanie_widok(request):
    return render(request, 'konta/logowanie.html')