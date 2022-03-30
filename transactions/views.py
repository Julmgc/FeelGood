from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from transactions.models import Transaction
from transactions.permissions import AdminGetPermission
from transactions.serializers import TransactionSerializer


class ListCreateTransaction(ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, AdminGetPermission]

    def create(self, request, *args, **kwargs):
        # criar as orders e a invoice
        return super().create(request, *args, **kwargs)


class RetrieveTransaction(RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, AdminGetPermission]
