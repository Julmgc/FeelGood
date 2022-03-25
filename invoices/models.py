from django.db import models
from sinta_se_bem.base_classes import GenericWithUUID


class Invoice(GenericWithUUID):
    number = models.CharField(max_length=44)
