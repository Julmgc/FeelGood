from django.db import models
from sinta_se_bem.base_classes import GenericWithUUID
# Create your models here.


class Category(GenericWithUUID):
    name = models.CharField(max_length=30)