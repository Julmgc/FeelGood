from uuid import uuid4
from django.db import models

# Create your models here.

class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    payment_method = models.CharField(max_length=20)
    card_number = models.CharField(max_length=20)
    cardholders_name = models.CharField(max_length=20)
    card_expiration_date = models.DateTimeField()
    cvv = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    # costumer_id = models.