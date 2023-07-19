from django.contrib import admin

# Register your models here.

from .models import Shopping_cart

class Cart_admin(admin.ModelAdmin):
    list_display = ('name','quantity','price','image')

admin.site.register(Shopping_cart,Cart_admin)