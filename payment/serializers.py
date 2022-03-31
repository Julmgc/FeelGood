from rest_framework import serializers
from django.utils.timezone import now
from rest_framework.exceptions import ValidationError

from payment.models import Payment
from users.serializer import UserSerializer
from transactions.exceptions import TransactionError


class PaymentSerializer(serializers.ModelSerializer):

    card_number_info = serializers.SerializerMethodField()
    customer = UserSerializer(required=False)
    card_number = serializers.CharField(write_only=True)

    class Meta:
        model = Payment
        fields = '__all__'

    def get_card_number_info(self, obj):
        return "*" * len(obj.card_number[:-4]) + obj.card_number[-4:]

    def validate(self, attrs):
        expiring_date = attrs.get('card_expiration_date')

        if (expiring_date - now().date()).days < 0:
            raise ValidationError({"error": ['This card is expired']})

        return super().validate(attrs)


class PaymentTransactionSerializer(serializers.Serializer):
    id = serializers.UUIDField()

    def validate(self, attrs):
        try:
            payment = Payment.objects.get(id=attrs["id"])
        except Payment.DoesNotExist:
            raise TransactionError({"detail": "Card was not found"}, code=404)
        if payment.card_expiration_date < now().date():
            raise TransactionError({"detail": "Card expired"}, code=400)
        return super().validate(attrs)
