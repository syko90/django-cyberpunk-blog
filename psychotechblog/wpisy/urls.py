from django.urls import path, re_path
from . import views

app_name = 'wpisy'

urlpatterns = [
    path('', views.wpisy_list, name= 'list'),
    path('wpisy/<slug>/', views.wpisy_detail, name='detail'),
    #re_path(r'^(?P<slug>[\w-]+)/$', views.wpisy_detail, name='detail'),    
    #path('<slug:slug>/', views.wpisy_detail, name= 'detail')
    #path('<slug>/', views.wpisy_detail, name="detail"),

]
