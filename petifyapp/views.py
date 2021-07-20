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
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        # Create user
        myuser = User.objects.create_user(
            username=username, email=email, password=password)
        myuser.first_name = firstname
        myuser.last_name = lastname

        myuser.save()
        # messages.info(request,"Your Petify account has been successfully created.")
        return redirect('login')
    else:
        return render(request, 'petify/signup.html')


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
        # request.session['mid'] = user.id
        # uid = request.session['mid']
        myuser = User.objects.get(myuser.username)
        if myuser.is_authenticated():
            myuser.first_name = newfirstname
            myuser.last_name = newlastname
            myuser.email = newemail
            myuser.save()
        # messages.info(request,"Your Petify account has been successfully created.")
            return redirect('home')
        else:
            return HttpResponse("Wrong Username")
    else:
        return render(request, 'petify/editprofile.html')


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
    centers = VaccinationCenter.objects.all()
    print(centers)
    param = {
        "centers": centers
    }
    return render(request, "petify/vaccination.html", param)






def vaccination_search(request):
    pass
