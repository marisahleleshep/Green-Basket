from django.contrib import admin

# Register your models here.

from .models import New_user

class Register_customer(admin.ModelAdmin):
    list_display = ("firstName","lastName","password","email","phoneNumber","address")

admin.site.register(New_user,Register_customer)