from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
import json


# Create your views here.

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cartItems = 0
        items = 0
    
    val = Product.objects.all()
    context = {
        "products":val,
        "cartItems":cartItems
    }
    return render(request,"store/store.html" , context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = OrderItem.objects.filter(order=order)
        cartItems = order.get_cart_items

    context ={
        "items":items,
        "order":order,
        "cartItems": cartItems
    }

    return render(request,"store/checkout.html" , context)




def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer , complete = False)
        items = order.orderitem_set.all().order_by( '-date_added')
        cartItems = order.get_cart_items
    else:
        cartItems = 0
        return redirect("login_page")
        
    context={
        "items":items,
        "order":order,
        "cartItems":cartItems
    }
    return render(request,"store/cart.html", context)

def signup_page(request):
    return render(request, "store/signup.html")    
def login_page(request):
    return render(request, "store/login.html") 

def signup(request):
    if request.method =="POST":
        username= request.POST["username"]
        name = request.POST["fname"]
        email = request.POST["email"]
        password = request.POST["password"]
        cpassword = request.POST["cpassword"]

        if password != cpassword:
            messages.warning(request, "Password does not match.")
            return redirect('signup_page')
        elif  User.objects.filter(email=email).exists():
                messages.warning(request, "Email is already in use.")
                return redirect('signup_page')
        else:
            user = User.objects.create_user(username=username,first_name = name, email = email, password=password)
            user.save()
            # log the new user in
            return redirect("login_page")
            
    

def log(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        usercheck = authenticate(username = username , password =password)
        if usercheck is not None:
            login(request, usercheck)
            messages.success(request,"Login successfully")
            return redirect("cart")
        else :
            print ("Login unsuccessful")
            return redirect("/")

def logout_this(request):
    logout(request)
    messages.success(request,'Logged out!')
    return redirect("/")


def addItem(request):
     data = json.loads(request.body)
     productId = data['productId']
     action = data['action']

     customer = request.user.customer
     product =Product.objects.get(id =productId)
     order, created = Order.objects.get_or_create(customer = customer, complete = False)

     orderItem,created = OrderItem.objects.get_or_create(order = order, product = product)

     if  action == 'add':
         orderItem.quantity = (orderItem.quantity +1 )
     elif action =='remove':
         orderItem.quantity = (orderItem.quantity -1)

     orderItem.save()

     if orderItem.quantity<=0:
              orderItem.delete()

     order.refresh_from_db()
     return JsonResponse("item added", safe=False)

        
    #  return JsonResponse("item added", safe=False)

    #  return render(request,"store/cart.html",context)
