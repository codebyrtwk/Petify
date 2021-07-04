from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages

def home(request):
	return render(request, 'petify/home.html')



#Signup page
def signup(request):
	if request.method =="POST":
		username = request.POST['username']
		fullname = request.POST['fullname']
		email = request.POST['email']
		password = request.POST['password']
		confirm_password = request.POST['confirm_password']

		#checks for errors


		#Create user
		myuser = User.objects.create_user(username=username , email = email , password=password)
		myuser.fullname = fullname
		myuser.save()

		messages.success(request,"Your Petify account has been successfully created.")
		return redirect('/')

	else:
		return render(request , 'petify/signup.html')
	
	
	


def login(request):
    return render(request , 'petify/login.html')

    
	

	
	


