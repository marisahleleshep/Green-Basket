from django.urls import path
from . import views

urlpatterns = [
    path('cart/add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='views_cart'),
]