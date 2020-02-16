from django.shortcuts import render
from . models import Wpis
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def wpisy_list(request):
    wpisy = Wpis.objects.all().order_by('date')
    return render(request, 'wpisy/wpisy_list.html', {'wpisy': wpisy} )

def wpisy_detail(request, slug):
    #return HttpResponse(slug)
    wpis = Wpis.objects.get(slug=slug)
    return render(request, 'wpisy/wpisy_detail.html', {'wpis': wpis})


@login_required(login_url= '/konta/logowanie/')
def wpis_nowy(request):
    return render(request, 'wpisy/wpis_nowy.html')