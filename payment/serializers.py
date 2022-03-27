from rest_framework import serializers
from django.utils.timezone import now
from rest_framework.exceptions import ValidationError

from payment.models import Payment
from users.serializer import UserSerializer


class PaymentSerializer(serializers.ModelSerializer):

    card_number_info = serializers.SerializerMethodField()
    customer = UserSerializer(required=False)

    class Meta:
        model = Payment
        exclude = ['card_number']

    def get_card_number_info(self, obj):
        return "*" * len(obj.card_number[:-4]) + obj.card_number[-4:]

    def validate(self, attrs):
        expiring_date = attrs.get('card_expiration_date')

        if (expiring_date - now().date()).days < 0:
            raise ValidationError({"error": ['This card is expired']})

        return super().validate(attrs)
