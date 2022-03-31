from rest_framework import serializers
from payment.models import Payment

from transactions.models import Transaction
from products.serializers import ProductsTransactionsSerializer
from payment.serializers import PaymentTransactionSerializer
from products.models import Product
from users.serializer import UserSerializer


class TransactionSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Transaction
        fields = '__all__'
        depth = 1


class TransactionValidate(serializers.Serializer):
    products = ProductsTransactionsSerializer(many=True)
    payment = PaymentTransactionSerializer()
    user = {}

    def __init__(self, instance=None, data=..., **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(instance, data, **kwargs)

    def validate(self, attrs):
        data = super().validate(attrs)
        products_info = []
        total = 0

        for product in data["products"]:
            product_found = Product.objects.get(id=product["id"])
            quantity = product["quantity"]
            price = product_found.price_client if not self.user.is_seller else product_found.price_seller
            amount = product["quantity"] * price
            total += amount
            products_info.append({
                "product":  product_found,
                "quantity": quantity,
                "amount": amount
            })

        payment = Payment.objects.get(id=data["payment"]["id"])

        return {"products_info": products_info, "payment": payment, "total": total}
