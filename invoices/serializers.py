from rest_framework import serializers
from .models import Invoice
from transactions.models import Transaction
from invoices.models import Invoice
from rest_framework.exceptions import ValidationError

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'number', 'transaction']
        depth = 1


