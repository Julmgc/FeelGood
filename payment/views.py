from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response, status
from rest_framework.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from payment.filters import IsOwnerFilterBackend

from payment.models import Payment
from payment.serializers import PaymentSerializer
from payment.permissions import BuyerPermission


class ListCreatePayment(ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, BuyerPermission]

    def create(self, request, *args, **kwargs):
        serialized = PaymentSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)

        check_in_db = self.queryset.filter(
            customer_id=request.user.uuid,
            card_number=request.data['card_number'],
            payment_method=request.data['payment_method'], is_active=True)
        if check_in_db:
            raise ValidationError(
                {'error': ["This card is already registered for this user"]})

        new_product = Payment.objects.create(
            **serialized.validated_data, customer=request.user)
        serializer = self.get_serializer(new_product)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        queryset = self.queryset.filter(customer_id=self.request.user.uuid, is_active=True)

        return queryset


class RetrieveRemovePayment(RetrieveDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    filter_backends = [IsOwnerFilterBackend]

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, BuyerPermission]

    lookup_url_kwarg = 'paymentId'
    lookup_field = 'id'

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
