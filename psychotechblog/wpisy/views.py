from django.shortcuts import render
from . models import Wpis
from django.http import HttpResponse

# Create your views here.
def wpisy_list(request):
    wpisy = Wpis.objects.all().order_by('date')
    return render(request, 'wpisy/wpisy_list.html', {'wpisy': wpisy} )

def wpisy_detail(request, slug):
    #return HttpResponse(slug)
    wpis = Wpis.objects.get(slug=slug)
    return render(request, 'wpisy/wpisy_detail.html', {'wpis': wpis})