from django.contrib import admin

from .models import Order

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display  = ("order_status","items","customer_information","payment_details")
admin.site.register(Order,OrderAdmin)