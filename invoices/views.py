from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.authentication import TokenAuthentication
from .serializers import InvoiceSerializer
from .models import Invoice
from users.permissions import AdminUser, AdminAndUser
from rest_framework.permissions import IsAuthenticated


class InvoiceGetView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, AdminUser]

    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceGetOneView(RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, AdminAndUser]

    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    lookup_url_kwarg = 'invoice_id'



