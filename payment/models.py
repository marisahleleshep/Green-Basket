from django.db import models

# Create your models here.

class Payment(models.Model):
    amount=models.CharField(max_length=32)
    payment_method=models.CharField(max_length=32)
    payment_date=models.DateField(auto_now_add=True)