from django.urls import path
from costumers.views import index

urlpatterns = [
  path('', index, name='costumers'),
]