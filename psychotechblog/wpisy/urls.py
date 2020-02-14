from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.wpisy_list),
    path('<slug:slug>/', views.wpisy_detail)

]
