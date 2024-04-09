from django.urls import path
from reports.views import index

urlpatterns = [
  path('', index, name='reports'),
]