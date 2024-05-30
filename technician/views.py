from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from technician.models import Tecnico

@login_required()
def index(request):
  tecnicos = Tecnico.objects.order_by("id").all()
  
  return render(request, 'technician/index.html', { "tecnicos" : tecnicos})