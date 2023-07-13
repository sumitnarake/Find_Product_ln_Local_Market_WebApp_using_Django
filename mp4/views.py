from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from product.models import Product
from shop.models import Shop
from contact.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


def addproduct(request):
    if request.method == 'POST':
        # Retrieve the form data from the request
        shop_name = request.POST.get('shop_name')
        city = request.POST.get('city', 'others')
        product_name = request.POST.get('product_name')
        username= request.POST.get('username')
        local_address=request.POST.get('local_address')
        product_price = float(request.POST.get('product_price'))
        product_availability = request.POST.get('product_availability', 'Not in stock')
        product_image = request.FILES.get('product_image')
        print(city)
        # Create a new Product instance
        new_product = Product(
            shop_name=shop_name,
            city=city,
            product_name=product_name,
            username=username,
            product_price=product_price,
            product_availability=product_availability,
            local_address=local_address,
            product_image=product_image
        )
        product=Product.objects.filter(username__contains=username)
        if Product.objects.filter(username=username, product_name=product_name).exists():
            error_message = "You have already added this product."
            return render(request, 'addproduct.html', {'error_message': error_message,'product':product})
        # Save the new product to the database
        else:
            new_product.save()
            shop_name=''
            city=''
            product_name=''
            username=''
            product_price=''
            product_availability=''
            local_address=''
            product_image=''
           
        
        return render(request,'addproduct.html',{'product':product})
    return render(request,'addproduct.html')
 
def homes(request):
    return render(request,'indexx.html')
    
    
def home(request):
    if request.method == 'POST':
        location=request.POST.get('location')
        name=request.POST.get('product')
        product=Product.objects.filter(product_name__contains=name,city__contains=location)
        return render(request,'result.html',{'product':product})
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        print(password)
        try:
            shop = Shop.objects.get(username=username, password=password)
            print("ok")
            request.session['shop_id'] = shop.id
            shop_name=shop.shop_name
            city=shop.city
            local_address=shop.local_address
            product=Product.objects.filter(username__contains=username)
            redirect_url = f'/addproduct/?username={username}&shop_name={shop_name}&city={city}&local_address={local_address}'
            return redirect(redirect_url)
        except Shop.DoesNotExist:
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})
    else:
        return render(request, 'login.html')
    return render(request, 'login.html')


def logout(request):
    logout(request)
    return redirect('/')  # replace 'home' with your desired redirect URL
    # return render(request,'login.html')



def register(request):
    if request.method == "POST":
        
        password=request.POST.get('password')
        print(request.POST)
        re_enter_password=request.POST.get('re_enter_password')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        shopkeeper_address=request.POST.get('shopkeeper_address')
        shop_category=request.POST.get('shop_category')
        city=request.POST.get('city')
        local_address=request.POST.get('local_address')
        shop_name=request.POST.get('shop_name')
        zip_code=request.POST.get('zip_code')
        country=request.POST.get('country')
        country_code=request.POST.get('country_code')
        print(country_code)
        print(country)
        phone_number=request.POST.get('phone_number')
        print(first_name)
        if  Shop.objects.filter(username__contains=username).exists():
            message = 'Username already exists, please choose a different one.'
            return render(request, 'register.html', {'message': message})
        else:
            if password==re_enter_password:
                new_shop =Shop(first_name=first_name,last_name=last_name,username=username,shopkeeper_address=shopkeeper_address,password=password,
                            re_enter_password=re_enter_password,shop_category=shop_category,city=city,
                            local_address=local_address,shop_name=shop_name,zip_code=zip_code,country=country,
                            country_code=country_code,phone_number=phone_number)
                new_shop.save()
                print("ok")
                return redirect('/')
            
            else:
                messages = 'password and re-enterpassword not match'
                return render(request,'register.html',{'messages': messages})
       
            
        
    return render(request,'register.html')

def contact(request):
    if request.method == 'POST':
        # Retrieve the form data from the request
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Create a new Product instance
        new_contact = Contact(name=name, email=email, subject=subject,message=message)

        # Save the new product to the database
        new_contact.save()
        return HttpResponse("Thank you")
    return render(request,'contact.html')


def update(request):
    if request.method=='POST':
        print("ok")
        username=request.POST.get('username')
        city=request.POST.get('city')
        local_address=request.POST.get('local_address')
        shop_name=request.POST.get('shop_name')
        print(username)
        print(city)
        print(shop_name)
        product=Product.objects.filter(username__contains=username)  
        my_dict = {
        'username': username,
        'shop_name': shop_name,
        'city': city, 
        'local_address':local_address,   
    }
        print("xyz")    
        return render(request,'modify.html',{'product':product,'username':my_dict})
    return render(request,'modify.html')  

# def modify(request,id):
    

#     if request.method == 'POST':
#         username=request.POST.get('username')
#         product_name=request.POST.get('product_name')
#         product_price=request.POST.get('product_price')
#         product_availability=request.POST.get('product_availability')
#         print(product_availability)
        
#         # product_name=request.POST.get('product_name')
#         product=Product(id=id,username=username,product_name=product_name,product_price=product_price, product_availability= product_availability)
#         product.save()
#         # product=Product.objects.filter(username__contains=username,product_name__contains=product_name)
#         products=Product.objects.filter(username__contains=username)

#         return render(request, 'addproduct.html', {'products':product})
        


#     return render(request, 'addproduct.html', {'products':product})

def modify(request,id):
    if request.method=="POST":
        username=request.POST.get('username')
        print(username)
        product_name=request.POST.get('product_name')
        product_price=request.POST.get('product_price')
        local_address=request.POST.get('local_address')
        product_availability=request.POST.get('product_availability')
        city=request.POST.get('city')
        shop_name=request.POST.get('shop_name')
        product_image = request.FILES.get('product_image')
        p=Product(id=id,username=username,product_name=product_name,product_price=product_price,local_address=local_address,city=city, product_availability= product_availability,shop_name=shop_name,product_image=product_image)
        p.save()
        print(city)
        print(shop_name)
        
        my_dict = {
        'username': username,
        'shop_name': shop_name,
        'city': city, 
        'local_address':local_address,   
    }
        product=Product.objects.filter(username__contains=username)
        
        
        

        return render(request, 'addproducts.html', {'product':product,'username':my_dict})
    return redirect(request,'modify.html')

    