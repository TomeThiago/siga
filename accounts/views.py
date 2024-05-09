from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django

def login(request):
  # if request.user:
  #   return HttpResponseRedirect(redirect_to="/dashbord")
  
  if request.method == 'GET':
    return render(request, 'accounts/login.html')
  elif request.method == 'POST':
    username = request.POST.get('user')
    password = request.POST.get('password')
    
    user = authenticate(username=username, password=password)
    
    if user:
      login_django(request, user)
      
      return HttpResponseRedirect(redirect_to="/dashboard")
    else:
      return HttpResponse('email or password is incorrect')
  

def register(request):
  if request.method == 'GET':
    return render(request, 'accounts/register.html')
  elif request.method == 'POST':
    name = request.POST.get('name')
    username = request.POST.get('user')
    password = request.POST.get('password')
    
    user = User.objects.filter(username=username).first()
    
    if user:
      return HttpResponse('User already registered')
    
    user = User.objects.create(username=username, password=password, name=name)
    user.save()
    
    return HttpResponse('User registration successful')

def logout(request):
  logout_django(request)
  
  return HttpResponseRedirect(redirect_to="/")