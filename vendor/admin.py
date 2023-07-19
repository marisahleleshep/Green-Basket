from django.contrib import admin

# Register your models here.

from .models import Vendor

class VendorAdmin(admin.ModelAdmin):
    list_display = ("name","business_name","contacts")

admin.site.register(Vendor,VendorAdmin)