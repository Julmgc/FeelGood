from rest_framework import serializers
from payment.models import Payment

from transactions.models import Transaction
from products.serializers import ProductsTransactionsSerializer
from payment.serializers import PaymentSerializer, PaymentTransactionSerializer
from products.models import Product
class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'
        depth=1
class TransactionValidate(serializers.Serializer):
    products = ProductsTransactionsSerializer(many=True)
    payment = PaymentTransactionSerializer()

    def validate(self, attrs):
        data = super().validate(attrs)
        products_info = []
        total = 0
        for product in attrs["products"]:
            product_found = Product.objects.get(id=product["id"])
            quantity = product["quantity"]
            amount = product["quantity"]* product_found.price_client
            total += amount
            products_info.append({"product":  product_found, "quantity": quantity, "amount": amount})
        
        payment = Payment.objects.get(id=attrs["payment"]["id"])

        return {"products_info": products_info, "payment": payment, "total": total}



        

# JSON da request:
# {
#     "products": [  ==> essa tem que fazer na mão
#         {
#             "id": "uuid",
#             "quantity": 1
#         },
#     ],
#     "payment": {    ==> acredito que o django consiga fazer essa validação sozinho
#         "id": "uuid"
#     }
# }
