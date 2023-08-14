from django.shortcuts import render, redirect
from .models import Shopping_cart
from inventory.models import Product

def add_to_cart(request, product_id):
    ShoppingCartForm = ShoppingCartForm.objects.get(id=product_id)
    user = request.user    
    cart, created = Shopping_cart.objects.get_or_create(user=user)    
    cart.products.add(ShoppingCartForm)    
    return redirect('view_cart')

def view_cart(request):
    user = request.user
    cart_items = Shopping_cart.objects.filter(user=user).prefetch_related('products')   
    total_price = sum(ShoppingCartForm.price * ShoppingCartForm.quantity for cart in cart_items for ShoppingCartForm in cart.ShoppingCartForm.all())  
    print("Cart Items:", cart_items)
    print("Total Price:", total_price)   
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'cart/view_cart.html', context)