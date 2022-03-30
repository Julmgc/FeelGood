from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from orders.models import Order
from transactions.filters import IsOwnerFilterBackend
from transactions.models import Transaction
from transactions.permissions import AdminGetPermission
from transactions.serializers import TransactionSerializer, TransactionValidate
from invoices.models import Invoice
import random
from rest_framework.views import Response, status
class ListCreateTransaction(ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, AdminGetPermission]

    def create(self, request, *args, **kwargs):
        serializer = TransactionValidate(data=request.data)
        serializer.is_valid(raise_exception=True)
        transaction = Transaction.objects.create(
            amount=serializer.validated_data["total"],
            payment=serializer.validated_data["payment"],
            user=request.user
        )
        for product in serializer.validated_data["products_info"]:
            Order.objects.create(quantity=product["quantity"], amount=product["amount"], product=product["product"], transaction=transaction, sale=product["product"].sale, customer=request.user)
            product["product"].quantity = product["product"].quantity - product["quantity"]
            product["product"].save()
        Invoice.objects.create(transaction=transaction, number="999"+str(int.from_bytes(random.randbytes(17),"big")))

        serializer = TransactionSerializer(transaction).data

        return Response(serializer, status=status.HTTP_201_CREATED)


class RetrieveTransaction(RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, AdminGetPermission]

    filter_backends = [IsOwnerFilterBackend]
    lookup_url_kwarg = "transactionId"
    lookup_field = "id"