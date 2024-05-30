from django.shortcuts import render
from notes.models import OrdemServico

def index(request):
  list_services = OrdemServico.objects.order_by("data_inicio").all()
  
  return render(request, 'notes/index.html', {'list_services': list_services})