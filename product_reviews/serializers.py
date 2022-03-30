from itertools import product
from rest_framework import serializers
from product_reviews.models import ProductReview
from users.serializer import UserSerializer
from products.models import Product
from rest_framework.exceptions import ValidationError
from orders.models import Order
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
            user_has_bougth_product = Order.objects.filter(customer=self.context['request'].user, product=get_product)
            
            if not user_has_bougth_product:
                raise ValidationError({"detail":"You can only review a product you have bought."})

            productReview = ProductReview.objects.create(**data_validated,user=self.context['request'].user, product=get_product)
            return productReview
        else:
             raise ValidationError({"product, score, comment":"This fields are required."})

class ProductReviewGetByIdAndPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = ['id', 'comment', 'score', 'user', 'product']
        extra_kwargs = {
            'product': {'read_only': True},
        }
        
    def update(self,instance,validated_data):
       
        
        user=self.context['request'].user
        product_review__id = self.context['view'].kwargs['productReviewId']
        product_review = ProductReview.objects.get(id=product_review__id)

        if product_review is not None:
            product_review_user_id = product_review.user.uuid

            if product_review_user_id == user.uuid:
                return super().update(instance,validated_data)
            else:
             raise ValidationError({'detail': 'You do not have permission to perform this action.'})
        

        return super().update(instance,validated_data)
    
   