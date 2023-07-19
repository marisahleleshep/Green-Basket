from django.db import models
from inventory.models import Product

# Create your models here.

class Shopping_cart(models.Model):
    products=models.ManyToManyField(Product)
    name = models.CharField(max_length = 20)
    quantity = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField()