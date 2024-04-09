from django.urls import path
from support.views import index

urlpatterns = [
  path('', index, name='support'),
]