from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from products.filters import ProductFilter
from products.exceptions import ProductNotFoundError
from products.models import Product
from products.permissions import AdminPermission, GetPermission
from products.serializers import ProductSerializer


class ListCreateProduct(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend]
    filter_class = ProductFilter

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated | GetPermission, AdminPermission]


class RetrieveUpdateDestroyProduct(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated | GetPermission, AdminPermission]

    lookup_url_kwarg = 'productId'
    lookup_field = 'id'

    def perform_destroy(self, instance):
        if not instance.is_active:
            raise ProductNotFoundError()
        instance.is_active = False
        instance.save()
