from django.db import models

from sinta_se_bem.base_classes import GenericWithUUID


class Invoice(GenericWithUUID):
    number = models.CharField(max_length=44)
    transaction = models.OneToOneField(
        'transactions.Transaction', related_name='invoice', on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey('users.User', related_name='invoices', on_delete=models.PROTECT, null=True)
    