from audioop import add
from cgi import test
from hashlib import new
from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
# My imports
from email import message
from unicodedata import name
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,get_user
from django.contrib import auth
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.utils.datastructures import MultiValueDictKeyError
from .models import AddProduct,Cart,Registration
# end imports



def login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            product_list=AddProduct.objects.all()
            context={'product_list':product_list}
            cart=request.session.get('cart')
            if not cart:
                request.session.cart={}
                
            return render(request,'shop/index.html',context)
        else:
            return redirect('login')
    return render(request, 'shop/login.html')


def log_out(request):
    logout(request)
    # return render(request,'shop/login.html')
    return redirect('/')


def log__out(request):
    logout(request)
    # return render(request,'shop/login.html')
    return redirect('ownerlogin')


def change_password(request):
    if request.method=='POST':
        new_pass=request.POST.get("new_password")
        u=User.objects.get(username=request.user.username)
        u.set_password(new_pass)
        u.save()
        print(new_pass)
        return redirect('index')            
    return render(request,'shop/change_password.html')


def register(request):
    if request.method =='POST':
        username=request.POST['username']
        emailid=request.POST['emailid']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password==confirm_password:
            obj=User.objects.create_user(username=username,email=emailid,password=password)
            obj.save()
            return render(request,'shop/login.html')
    return render(request, 'shop/register.html')


def index(request): 
    cart=request.session.get('cart')
    if not cart:
        request.session['cart']={}
    print(request.session.get('cart').keys)    
    product_list=AddProduct.objects.all()
    context={'product_list':product_list}
    return render(request,'shop/index.html',context)     
    


def forget_pass(request):
    return render(request, 'shop/forget_pass.html')


def terms(request):
    return render(request, 'shop/terms.html')


def about(request):
    return render(request,'shop/about.html')


def ownerlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        if username=="owner":
            if password=="owner":
                product_list=AddProduct.objects.all()
                context={'product_list':product_list}
                return render(request,'shop/ownerindex.html',context)
            
            else:
                print("password is incorrect")
        else:
            print("username is incorrect")
    return render(request,'shop/ownerlogin.html')


def ownerindex(request):
    product_list=AddProduct.objects.all()
    context={'product_list':product_list}
    return render(request,'shop/ownerindex.html',context)


def add_products(request):
    if request.method=="POST":
        
        product_name=request.POST.get('Product_Name')
        product_description=request.POST.get('Product_Description')    
        product_specifications=request.POST.get('Specifications')    
        product_stock=request.POST.get('Stock')    
        product_price=request.POST.get('Price')  
        print(product_name)
        if len(request.FILES) != 0:
            product_image=request.FILES['img[]']

        print(product_name,product_description,product_specifications,product_stock,product_price)
        
        object=AddProduct(product_name=product_name,product_description=product_description,product_specifications=product_specifications,product_stock=product_stock,product_price=product_price,product_image=product_image)
        object.save()
        return redirect('add_products')
    return render(request,'shop/add_products.html')
    

def product_list(request):
    product_list=AddProduct.objects.all()
    context={'product_list':product_list}
    return render(request,'shop/product_list.html',context)


def update_product(request, id):
    prod= AddProduct.objects.get(id=id)
    if request.method=="POST":
        if len(request.FILES) != 0:
            # if len(prod.product_image) >0:
            #     os.remove(prod.product_image.path)
            prod.product_image= request.FILES['img[]']
        prod.product_name=request.POST.get('Product_Name')
        prod.product_description=request.POST.get('Product_Description')
        prod.product_specifications=request.POST.get('Specifications')
        prod.product_stock=request.POST.get('Stock')
        prod.product_price=request.POST.get('Price')
        prod.save()
        # messages.success(request, "Prouduct Updated Successfully")
        return redirect('product_list')
    context ={'prod':prod}    
    return render(request,'shop/update_product.html',context)
    
    
def delete_product(request,id):
    product=AddProduct.objects.get(id=id)
    product.delete()
    return redirect('product_list')


def cart(request,id):
    if request.method=='POST':
        product= AddProduct.objects.get(id=id)
        user=request.user
        user2=user.id
        prod=Cart()
        product_name=product.product_name
        product_price=product.product_price
        prod2=Cart.objects.filter(usercart=user2,product_name=product_name)
        prod3=Cart.objects.filter(product_name=product_name)
        if len(prod2)>0:
            if len(prod3)>0:
                prod4= Cart.objects.get(usercart=user2,product_name=product_name)
                if prod4:
                    quantity=prod4.quantity
                    quantity=quantity+1
                    print(quantity)
                    prod4.quantity=quantity
                    # print(prod.quantity)
                    # prod=Cart(quantity=quantity)
                    prod4.save()
            else:
                quantity=1
                prod=Cart(product_name=product_name,product_price=product_price,usercart=user,quantity=quantity)
                prod.save()
        else:
                quantity=1
                prod=Cart(product_name=product_name,product_price=product_price,usercart=user,quantity=quantity)
                prod.save()
                
        pro_duct= AddProduct.objects.get(id=id)
        pro_duct.product_stock=pro_duct.product_stock - 1 
        if pro_duct.product_stock > 0:
            pro_duct.save()
        else:
            pro_duct.product_stock=0
            pro_duct.save()
        return redirect('index')
    
    


def showcart(request):
    user=request.user
    user2=user.id
    product_list= Cart.objects.filter(usercart=user2)
    print(product_list)
    context={'product_list':product_list}
    return render(request,'shop/showcart.html',context)


def remove(request,id):
    product=Cart.objects.get(id=id)
    prod=product.quantity
    prod_name=product.product_name
    p_name=AddProduct.objects.get(product_name=prod_name)
    p_name.product_stock=p_name.product_stock+product.quantity
    p_name.save
    product.delete()
    return redirect('showcart')
    
    
def usercartlist(request):
    orders=Cart.objects.all()
    context={'orders':orders}  
    return render(request,'shop/usercartlist.html',context)


def profile(request):
    user=request.user
    if request.method=='POST':
        userprofile=Registration.objects.filter(email=user.email)
        
        # __________________update profile____________________
        
        if len(userprofile)>0:
            userprof=Registration.objects.get(email=user.email)
            name=request.POST.get('name')
            dob=request.POST.get('dob')
            # dob=request.POST['dob']
            mobile_no=request.POST.get('mobile_no')
            email=request.POST.get('email')
            address=request.POST.get('address')
            # print(email,dob,address)
            
            if len(request.FILES) != 0:
                userprof.profile_pic=request.FILES['img[]']    
            else:
                pass
            
            if userprof.name==name:
                pass
            else:
                print(name)
                userprof.name=request.POST.get('name')
            
            if userprof.dob == "":
                pass
            else:
                userprof.dob=request.POST.get('dob')
            
            if userprof.mobile_no == mobile_no:
                pass
            else:
                userprof.mobile_no=request.POST.get('mobile_no')
                
            if userprof.address == address:
                pass
            else:
                userprof.address=request.POST.get('address')
                
            userprof.save()
            prof=Registration.objects.get(email=user.email)
            context={'prof':prof}
            return render(request,'shop/profile.html',context)
        
        # ______________________registration______________
        
        else:
            if len(request.FILES) != 0:
                profile_pic=request.FILES['img[]']    
            name=request.POST.get('name')
            dob=request.POST.get('dob')
            mobile_no=request.POST.get('mobile_no')
            email=request.POST.get('email')
            address=request.POST.get('address')
            print(name,dob,mobile_no,email,address)
            obj=Registration(profile_pic=profile_pic,name=name,dob=dob,mobile_no=mobile_no,email=email,address=address)
            obj.save()      
            return redirect('index')

        
    
    try:
        user=request.user
        prof=Registration.objects.get(email=user.email)
        # print(prof.email,prof.address)
        context={'user':user,'prof':prof}
        return render(request,'shop/profile.html',context)
    except:
        pass
    return render(request,'shop/profile.html')    



def customer_data(request):
    data=Registration.objects.all()
    context={'data': data}
    return render(request,'shop/customer_data.html',context)

