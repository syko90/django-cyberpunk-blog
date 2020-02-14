from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wpisy/', include('wpisy.urls')),
    path('onas/', views.onas),
    path('',views.blog),
]

urlpatterns += staticfiles_urlpatterns()