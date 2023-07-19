from django.contrib import admin

# Register your models here.

from .models import Product
class Category_name(admin.ModelAdmin):
    list_display=["name"]

admin.site.register(Product,Category_name)