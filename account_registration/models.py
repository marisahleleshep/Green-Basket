from django.db import models

# Create your models here.
class New_user(models.Model):
    firstName=models.CharField(max_length=32)
    lastName=models.CharField(max_length=32)
    password=models.DecimalField(max_digits=8,decimal_places=2)
    email=models.CharField(max_length=30)
    phoneNumber=models.CharField(max_length=30)
    address  = models.CharField(max_length=20)