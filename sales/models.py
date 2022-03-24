from django.db import models
from sinta_se_bem.base_classes import GenericWithUUID


class Sale(GenericWithUUID):
    dicount_percentage=models.FloatField()
    is_active = models.BooleanField(default=True)
    initial_datetime = models.DateTimeField()
    final_datetime = models.DateTimeField()


