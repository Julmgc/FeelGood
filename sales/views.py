from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.authentication import TokenAuthentication

from users.permissions import AdminSale
from sales.models import Sale
from sales.serializers import SaleSerializer, SaleGetByIdAndPatchSerializer


class SaleListCreateView(ListCreateAPIView):
    authentications_classes = [TokenAuthentication]
    permission_classes = [AdminSale]

    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SaleGetByIdAndPatchSerializer
        return super().get_serializer_class()


class SaleIdView(RetrieveUpdateAPIView):
    authentications_classes = [TokenAuthentication]
    permission_classes = [AdminSale]

    queryset = Sale.objects.all()
    serializer_class = SaleGetByIdAndPatchSerializer

    lookup_url_kwarg = 'sale_id'
