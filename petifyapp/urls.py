from django.urls import path
from . import views

urlpatterns = [
    path("" , views.home , name = "home"),
    path("signup/" , views.signup , name = "signup"),
    path('login/' , views.login , name = 'login'),
    path('logout/' , views.logout , name = 'logout'),
    path('vendorlogin/' , views.vendorlogin , name = 'vendorlogin'),
    path('becomevendor/' , views.becomevendor , name = 'becomevendor'),
    path("editprofile/" , views.editprofile , name = 'editprofile'),
    path("vaccination/" , views.vaccination , name ="vaccination"),
    path('vaccination_search' , views.vaccination_search , name ="vaccination_search")
    
    

    ]