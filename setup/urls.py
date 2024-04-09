from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('dashboard', include('dashboard.urls')),
    path('emissao-notas', include('notes.urls')),
    path('relatorios', include('reports.urls')),
    path('calculo-valores', include('calculation.urls')),
    path('suporte', include('support.urls')),
]
