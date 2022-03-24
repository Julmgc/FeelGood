from django.db import models
from sinta_se_bem.base_classes import GenericWithUUID
# Create your models here.

class Payment(GenericWithUUID):
    payment_method = models.CharField(max_length=20)
    card_number = models.CharField(max_length=20)
    cardholders_name = models.CharField(max_length=20)
    card_expiration_date = models.DateTimeField()
    cvv = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    costumer_id = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name='payment_id')