import imp
from itertools import product
from rest_framework import serializers
from product_reviews.models import ProductReview
from users.serializer import UserSerializer
from products.serializers import ProductSerializer

class ProductReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    product = ProductSerializer(read_only=True)
    class Meta:
        model = ProductReview
        fields = ['id', 'comment', 'score', 'user', 'product']
        extra_kwargs = {
            'name': {
                'validators': []
            }
        }


class ProductReviewGetByIdAndPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = ['id', 'comment', 'score', 'user', 'product']

    def update(self,instance,validated_data):
        return super().update(instance,validated_data)
    
   