from django.db import models
from inventory.models import Product
from django.contrib.auth.models import User
from django.shortcuts import render,redirect



# Create your models here.
class Shopping_cart(models.Model):
    products=models.ManyToManyField(Product)
    name = models.CharField(max_length = 20)
    quantity = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField()

def addProduct(request):
        user = request.user
        product_id = request.GET.get('product_id')
        product_cart = Product.objects.get(id=product_id)
        Shopping_cart(user=user, product=product_cart).save()
        return render(request, 'cart/addtocart.html')

def delete_cart_item(request):
        cart_item_id = request.GET.get('cart_item_id')
        CartItem.objects.filter(cart__user=request.user.id,id=cart_item_id)
        return render(request, your_template)