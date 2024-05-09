from django.urls import path
from accounts.views import login, logout, register

urlpatterns = [
  path('', login, name='login'),
  path('logout', logout, name='logout'),
  path('create-account', register, name='register'),
]