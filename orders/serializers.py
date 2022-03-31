from rest_framework import serializers

from .models import Order


class OrderGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'quantity', 'amount', 'product', 'transaction', 'customer']
        depth = 1
