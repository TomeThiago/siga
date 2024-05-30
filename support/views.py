from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SuporteForm

def index(request):
  form = SuporteForm()
  
  return render(request, 'support/index.html', { 'form': form})

def create_support(request):
  if(request.method == 'POST'):
    form = SuporteForm(request.POST)
    
    if form.is_valid():
      form.save()
      
      print ('save')
        
      return HttpResponseRedirect(redirect_to="/support")
  else:
    form = SuporteForm()
    
    return render(request, 'support/index.html', {'form': form})