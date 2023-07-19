from django.db import models
from customer.models import Customer
from cart.models import Shopping_cart
from shipping.models import Shipping

# Create your models here.
class Order(models.Model):
    order_status  = models.CharField(max_length=10)
    items = models.CharField(max_length=10)
    customer_information  = models.CharField(max_length=15)
    payment_details = models.CharField(max_length=32)


    customer=models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
    cart=models.OneToOneField(Shopping_cart,null=True,on_delete=models.CASCADE)
    shipping=models.OneToOneField(Shipping,null=True,on_delete=models.CASCADE)