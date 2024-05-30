from django.shortcuts import render

def index(request):
  return render(request, 'reports/index.html')

def create_report(request):
  if(request.method == 'POST'):
    description = request.POST.get('description')