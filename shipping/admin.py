from django.contrib import admin

# Register your models here.
from .models import Shipping

class ShippingAdmin(admin.ModelAdmin):
    list_display = ("address","contact","date")

admin.site.register(Shipping,ShippingAdmin)