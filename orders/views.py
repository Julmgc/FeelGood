from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .permissions import AdminAndSellerUser
from .models import Order
from .serializers import OrderGetSerializer


class OrderGetView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, AdminAndSellerUser]

    queryset = Order.objects.all()
    serializer_class = OrderGetSerializer


class OrderGetOneView(RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, AdminAndSellerUser]

    queryset = Order.objects.all()
    serializer_class = OrderGetSerializer
    lookup_url_kwarg = 'order_id'


class OrderGetOneTransactionView(RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, AdminAndSellerUser]

    queryset = Order.objects.all()
    serializer_class = OrderGetSerializer
    lookup_url_kwarg = 'transaction_id'
    lookup_field = 'transaction_id'
