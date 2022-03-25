from django.db import models
from django.core import validators
from sinta_se_bem.base_classes import GenericWithUUID


class Transaction(GenericWithUUID):
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    payment = models.ForeignKey(
        "payment.Payment", on_delete=models.CASCADE, related_name="transaction_id")
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="transaction_id", null=True)
