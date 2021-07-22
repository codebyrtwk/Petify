from django.db import models


# Create your models here.
class user(models.Model):
	username = models.CharField(max_length = 20)
	fullname = models.CharField(max_length = 30)
	email = models.EmailField(max_length = 100)
	password =  models.CharField(max_length=20)


# class Products(models.Model):
#     product_id = models.AutoField(primary_key=True)
# 	product_name = models.CharField(max_length=50)
# 	cat
    
# class MySpecialUser(models.Model):
#     vendorusername = models.OneToOneField(
#         user,
#         on_delete=models.CASCADE,
# 		primary_key = True
#     )
	

class VaccinationCenter(models.Model):
	centerid = models.AutoField(primary_key = True)
	centername = models.CharField(max_length=50)
	centerlocation = models.CharField(max_length=100)
	centerpincode = models.IntegerField()
	centerphone = models.IntegerField()
	image= models.ImageField(upload_to = "petify/images" , default = "")
	
	def __str__(self):return self.centername
	 
