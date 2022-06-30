from django.db import models
from django.contrib.auth.models import User
# Create your models here.

    
class AddProduct(models.Model):
    product_name=models.CharField(max_length=50)
    product_price=models.IntegerField()
    product_description=models.TextField()
    product_specifications=models.TextField()
    product_stock=models.IntegerField()
    product_image=models.ImageField(upload_to='filepath', null=True, blank=True)
    
    def __str__(self):
        return self.product_name
    
    
class Cart(models.Model):
    product_name=models.CharField(max_length=50)
    product_price=models.IntegerField()
    usercart=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    quantity=models.IntegerField()
    
    def __str__(self):
       return self.product_name
    
class Registration(models.Model):
    profile_pic=models.ImageField(upload_to='Profile_Images', null=True, blank=True)
    name=models.CharField(max_length=50,null=True)
    dob=models.DateField(max_length=8,null=True, blank=True)
    mobile_no=models.BigIntegerField(null=True)
    email=models.EmailField(null=True)
    address=models.TextField(null=True)
    
    def __str__(self):
        return self.name
    
    