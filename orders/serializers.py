from rest_framework import serializers
from .models import Order

class OrderGetSerializer(serializers.Modelserializer):
    class Meta:
        model = Order
        fields = ['id','quantity','amount','product']
        depth = 1
        
