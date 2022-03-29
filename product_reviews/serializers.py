from rest_framework import serializers
from product_reviews.models import ProductReview
from users.serializer import UserSerializer
from products.models import Product
from rest_framework.exceptions import ValidationError

class ProductReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
 
    class Meta:
        model = ProductReview
        fields = ['id', 'comment', 'score', 'user', 'product']
        extra_kwargs = {
            'product': {
                'required': True
            }
        }
        depth = 1

    def create(self,validated_data):
        data_validated = {"comment": validated_data["comment"], "score": validated_data["score"]}
        review_product = self.context['view'].request.data.get('product', None)
        if review_product is not None:
            get_product = Product.objects.get(id=review_product)
        
            productReview = ProductReview.objects.create(**data_validated,user=self.context['request'].user, product=get_product)
            return productReview
        else:
             raise ValidationError({"product, score, comment":"This fields are required."})

class ProductReviewGetByIdAndPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = ['id', 'comment', 'score', 'user', 'product']

    def update(self,instance,validated_data):
        
        id =  self.context['view'].kwargs['productReviewId']
        user=self.context['request'].user
        if user.uuid == id:
            return super().update(instance,validated_data)
        else:
            raise ValidationError({'detail': 'No Permission.'})
   