from django.db import models

from sinta_se_bem.base_classes import GenericWithUUID
from django.core.validators import MaxValueValidator, MinValueValidator


class ProductReview(GenericWithUUID):
    comment = models.CharField(max_length=255)
    score = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    user = models.ForeignKey(
        'users.User', related_name='productReview', on_delete=models.PROTECT)
    product = models.ForeignKey(
        'products.Product', related_name='productReview', on_delete=models.CASCADE)
