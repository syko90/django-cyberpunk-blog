from django.shortcuts import render
from . models import Wpis

# Create your views here.
def wpisy_list(request):
    wpisy = Wpis.objects.all().order_by('date')
    return render(request, 'wpisy/wpisy_list.html', {'wpisy': wpisy} )