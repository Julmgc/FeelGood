from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.authentication import TokenAuthentication

from users.permissions import ClientOrSellerProductReview
from product_reviews.models import ProductReview
from product_reviews.serializers import ProductReviewSerializer, ProductReviewGetByIdAndPatchSerializer


class ProductReviewListCreateView(ListCreateAPIView):
    authentications_classes = [TokenAuthentication]
    permission_classes = [ClientOrSellerProductReview]

    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductReviewGetByIdAndPatchSerializer
        return super().get_serializer_class()


class ProductReviewIdView(RetrieveUpdateAPIView):
    authentications_classes = [TokenAuthentication]
    permission_classes = [ClientOrSellerProductReview]

    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewGetByIdAndPatchSerializer

    lookup_url_kwarg = 'productReviewId'
