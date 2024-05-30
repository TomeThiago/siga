from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from costumers.models import Cliente

@login_required()
def index(request):
  clientes = Cliente.objects.order_by("id").all()
  
  return render(request, 'costumers/index.html', { "clientes" : clientes})