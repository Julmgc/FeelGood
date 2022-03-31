from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.views import APIView

from category.permissions import CanCreateCategory, CanGetCategory
from course_link.permissions import AdminPermission


from .models import Category
from .serializers import CategorySerializer
from products.models import Product
from rest_framework.response import Response
from products.serializers import ProductSerializer
from rest_framework import status

class CategoryViews(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [CanCreateCategory]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SpecificCategoryViews(RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [CanGetCategory]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_url_kwarg = 'category_id'

class CategoryAndProdutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AdminPermission]
    def post(self, request, category_id=''):
        try:
            course = Category.objects.get(id=category_id)
            product_id = request.data['product_id']
            product = Product.objects.get(id=product_id)
            product.categories.add(course)
            product.save()

            return Response(ProductSerializer(product).data, status=status.HTTP_200_OK)
        except (Category.DoesNotExist, Product.DoesNotExist):
            return Response({'detail': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
