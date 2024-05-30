from django.urls import path
from support.views import index, create_support

urlpatterns = [
  path('', index, name='support'),
  path('create_support', create_support, name='create_support'),
]