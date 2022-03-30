from rest_framework import serializers
from .models import Invoice


class InvoiceSerializer(serializers.Modelserializer):
    class Meta:
        model = Invoice
        fields = ['id', ]
        depth = 1
