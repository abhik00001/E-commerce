from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)

    def  __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    digital = models.BooleanField(default = False, null=True , blank=False)
    image = models.ImageField(upload_to="product_images", null= True, blank=True ,  max_length=360)

    def __str__(self):
        return self.name
    
    # for protect the site if images is not available
    @property
    def imageURL(self):
         if self.image:
             return '/media/%s' % (self.image)
         else:
            return "/static/images/2+placeholder.png"
    
class Order(models.Model):
    customer = models.ForeignKey(Customer,null = True, blank =True ,on_delete=models.SET_NULL)
    date_ordered = models.DateTimeField( auto_now_add=True)
    complete = models.BooleanField(default = False, null=True , blank=False)
    transaction_id = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_items(self):
        items= self.orderitem_set.all()
        total = sum([item.quantity for item in items])
        return total
    @property
    def get_cart_total(self):
        items = self.orderitem_set.all()
        total = sum([item.get_total for item in items])
        return total
    
        
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product,  on_delete=models.SET_NULL  , null= True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL , null = True)
    quantity = models.IntegerField(default = 0 , null = True , blank = True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.quantity * self.product.price
        return total

class Shipping_Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null= True)
    order = models.ForeignKey(Order,  on_delete=models.SET_NULL , null= True)  
    address = models.CharField(max_length=200 , null =False)
    city = models.CharField(max_length = 100 , null=False)
    state = models.CharField(max_length = 100 , null=False)
    pincode = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
    
