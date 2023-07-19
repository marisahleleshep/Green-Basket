from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=20)

    def all_names():
        return Product.objects.all()
    def __str__(self):
        return self.name