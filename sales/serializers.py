from rest_framework import serializers

from sales.models import Sale


class SaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sale
        fields = ['id', 'discount_percentage', 'is_active',
                  'initial_datetime', 'final_datetime']
        read_only_fields = ['is_active']
        extra_kwargs = {
            'name': {
                'validators': []
            }
        }


class SaleGetByIdAndPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id', 'discount_percentage', 'is_active',
                  'initial_datetime', 'final_datetime']

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
