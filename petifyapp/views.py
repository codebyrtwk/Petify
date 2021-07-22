from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import VaccinationCenter
import math


def home(request):
    return render(request, 'petify/home.html')


# Signup page
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        #send confirmation email
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            user = User.objects.create_user(
                username=username, password=password, email=email, first_name=firstname, last_name=lastname)
            user.save()
            return HttpResponse("You are at signup page")
        else:
            return HttpResponse("Password does not match")

        #check if username already exists
        if username == "" or username in user.objects.all():
            return HttpResponse("Username already exists")
        else:
            return redirect('home')

    return render(request, "petify/signup.html")



# LOGIN PAGE
def login(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        # AUTHENTICATING A USER
        user = auth.authenticate(
            username=loginusername, password=loginpassword)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Invalid Credentials")
    else:
        return render(request, "petify/login.html")


# LOGOUT PAGE
def logout(request):
    if request.method == 'GET':
        auth.logout(request)
    return redirect('home')

# Edit User Profile
@login_required
def editprofile(request):
    if request.method == "POST":
        newfirstname = request.POST['firstname']
        newlastname = request.POST['lastname']
        newemail = request.POST['email']
        myuser = request.user
        myuser.first_name = newfirstname
        myuser.last_name = newlastname
        myuser.email = newemail
        myuser.save()
        #check if username already exists
        for username in User.objects.all():
            if username.username == myuser.username:
                #messages popup
                messages.info(request, "Username already exists")
                return redirect('editprofile')
            else :
                messages.info(request, "Your profile has been updated successfully")
                return redirect('home')

    else:
        return render(request, "petify/editprofile.html")

    



# Become vendor page owner
def becomevendor(request):
    return render(request, "petify/becomevendor.html")


# vendorlogin PAGE
def vendorlogin(request):
    if request.method == "POST":
        vendorusername = request.POST['vendorusername']
        vendorpassword = request.POST['vendorpassword']
        vendoraddress = request.POST['Enter Address']
        # AUTHENTICATING A USER
        vendoruser = auth.authenticate(
            username=vendorusername, password=vendorpassword)
        if vendoruser is not None:
            auth.login(request, vendoruser)
            return HttpResponse("You are at Merchant page")
        else:
            return HttpResponse("Invalid Credentials")

    return render(request, "petify/vendorlogin.html")


# Vaccination PAGE
def vaccination(request):
    centers = VaccinationCenter.objects.all().order_by('centername')
    print(centers)
    param = {
        "centers": centers
    }
    return render(request, "petify/vaccination.html", param)

#search on vaccination page based on center location        
def vaccination_search(request):
    if request.method == "POST":
        location = request.POST['searchcenter']
        centers = VaccinationCenter.objects.all().order_by('centername')
        #add center into result variable based on query string
        result = centers.filter(centerlocation__icontains=location )
        param = {
            "centers": result 
        }
        return render(request, "petify/vaccination.html", param)
    else:
        return redirect('vaccination')


       
    