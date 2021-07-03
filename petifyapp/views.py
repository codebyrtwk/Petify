from django.shortcuts import render

def home(request):
	return render(request, 'petify/home.html')

def signup(request):
	return render(request , 'petify/signup.html')

def login(request):
	return render(request , 'petify/login.html')

