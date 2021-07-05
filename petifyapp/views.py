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
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		email = request.POST['email']
		password = request.POST['password']
		confirm_password = request.POST['confirm_password']

		

			


		#Create user
		myuser = User.objects.create_user(username=username , email = email , password=password)
		myuser.first_name = firstname
		myuser.last_name = lastname
		myuser.save()
		# messages.info(request,"Your Petify account has been successfully created.")
		return redirect('login')
	else:
		return render(request , 'petify/signup.html')
	
	
	



#LOGIN PAGE
def login(request):

	if request.method =="POST":
		loginusername = request.POST['loginusername']
		loginpassword = request.POST['loginpassword']
		#AUTHENTICATING A USER
		user = auth.authenticate(username = loginusername , password = loginpassword)
		if user is not None:
			auth.login(request , user)
			return redirect('home')
		else:
			return HttpResponse("Invalid Credentials")
	else :
		return render(request , "petify/login.html")



#LOGOUT
def logout(request):
    if request.method =="POST":
    	auth.logout(request)

    
	

	
	


