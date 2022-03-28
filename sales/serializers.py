from rest_framework import serializers
from sales.models import Sale
from users.serializer import UserSerializer

class SaleSerializer(serializers.ModelSerializer):
    seller = UserSerializer(read_only=True)
    class Meta:
        model = Sale
        fields = ['id', 'discount_percentage', 'is_active', 'initial_datetime','final_datetime']
        read_only_fields = [ 'is_active']
        extra_kwargs = {
            'name': {
                'validators': []
            }
        }
        depth = 1


    def create(self,validated_data):
        sale = Sale.objects.create(**validated_data,seller=self.context['request'].user)
        return sale


class SaleGetByIdAndPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id', 'discount_percentage', 'is_active', 'initial_datetime','final_datetime']

    def update(self,instance,validated_data):
        return super().update(instance,validated_data)
    
   