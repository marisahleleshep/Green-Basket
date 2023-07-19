from django.db import models

# Create your models here.
class Shipping(models.Model):
    address=models.CharField(max_length=30)
    contact=models.CharField(max_length=20)
    date=models.DateField()