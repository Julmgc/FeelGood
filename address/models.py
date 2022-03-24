from django.db import models

# Create your models here.

class Address(models.Model):
    street = models.CharField(max_length=30)
    cep = models.CharField(max_length=9)
    house_number = models.CharField(max_length=5)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=30)
