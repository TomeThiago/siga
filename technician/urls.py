from django.urls import path
from technician.views import index

urlpatterns = [
  path('', index, name='technician'),
]