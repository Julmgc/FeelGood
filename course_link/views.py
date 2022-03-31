from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from products.models import Product
from .permissions import AdminPermission
from .models import CourseLink
from products.serializers import ProductSerializer
from .serializer import CourseLinkSerializer


class CourseLinkCreateAndList(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AdminPermission]

    queryset = CourseLink.objects.all()
    serializer_class = CourseLinkSerializer


class CourseLinkUpdateAndListOne(RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AdminPermission]

    queryset = CourseLink.objects.all()
    serializer_class = CourseLinkSerializer
    lookup_url_kwarg = 'course_id'


class CourseAndProdut(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AdminPermission]
    def post(self, request, courseId=''):
        try:
            course = CourseLink.objects.get(id=courseId)
            product_id = request.data['product_id']
            product = Product.objects.get(id=product_id)
            product.course_links.add(course)
            product.save()

            return Response(ProductSerializer(product).data, status=status.HTTP_200_OK)
        except (CourseLink.DoesNotExist, Product.DoesNotExist):
            return Response({'detail': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
