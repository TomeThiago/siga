from django.urls import path
from calculation.views import index

urlpatterns = [
  path('', index, name='calculation'),
]