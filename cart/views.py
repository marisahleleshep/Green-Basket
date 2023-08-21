from django.shortcuts import render, redirect
from .models import Shopping_cart
from inventory.models import Product
from django.contrib.auth.models import User


def add_to_cart(request, product_id):
    ShoppingCartForm = ShoppingCartForm.objects.get(id=product_id)
    user = request.user    
    cart, created = Shopping_cart.objects.get_or_create()    
    cart.products.add(ShoppingCartForm)    
    return redirect('views_cart')

def view_cart(request):
    user = request.user
    cart_items = Shopping_cart.objects.filter().prefetch_related('products')   
    total_price = sum(ShoppingCartForm.price * ShoppingCartForm.quantity for cart in cart_items for ShoppingCartForm in cart.ShoppingCartForm.all())  
    print("Cart Items:", cart_items)
    print("Total Price:", total_price)   
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'cart/views_cart.html', context)

def addProduct(request):
        user = request.user
        product_id = request.GET.get('product_id')
        product_cart = Product.objects.get(id=product_id)
        Shopping_cart( product=product_cart).save()
        return render(request, 'cart/addtocart.html')