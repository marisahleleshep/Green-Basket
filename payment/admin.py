from django.contrib import admin

# Register your models here.

from.models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display=("amount","payment_method","payment_date")

admin.site.register(Payment,PaymentAdmin)