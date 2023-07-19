from django.db import models

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=30)
    business_name = models.CharField(max_length=20)
    contacts = models.CharField(max_length=13)
    


