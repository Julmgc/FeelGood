from django.db import models
from django.core import validators
from sinta_se_bem.base_classes import GenericWithUUID


class Product(GenericWithUUID):
    name= models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price_client = models.FloatField()
    price_seller = models.FloatField()
    quantity = models.IntegerField(default=0, validators=[validators.MinValueValidator(0)])
    expiration_date = models.DateField()
    sale=models.ForeignKey('sales.Sale',on_delete=models.CASCADE,null=True)