from django.db import models

from sinta_se_bem.base_classes import GenericWithUUID


class Order(GenericWithUUID):

    quantity = models.PositiveIntegerField()
    amount = models.DecimalField(decimal_places=2, max_digits=19)
    product = models.ForeignKey('products.Product', related_name='orders', on_delete=models.PROTECT)
    transaction = models.ForeignKey('transactions.Transaction', related_name='orders', on_delete=models.PROTECT)
    sale = models.ForeignKey('sales.Sale', related_name='orders', on_delete=models.PROTECT, null=True)
