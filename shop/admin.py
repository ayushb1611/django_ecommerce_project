from django.contrib import admin

# Register your models here.
from .models import AddProduct,Cart,Registration

class AddProductAdmin(admin.ModelAdmin):
    admin.site.register(AddProduct)
    
    

class CartAdmin(admin.ModelAdmin):
    admin.site.register(Cart)
    
   
    

class RegistrationAdmin(admin.ModelAdmin):
    admin.site.register(Registration)
    
