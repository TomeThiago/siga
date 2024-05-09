from django.shortcuts import render

def index(request):
  list_services = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
  
  return render(request, 'notes/index.html', {'list_services': list_services})