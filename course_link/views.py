from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .serializer import CourseLinkSerializer
from .models import CourseLink
from rest_framework.authentication import TokenAuthentication
from .permissions import AdminPermission
from rest_framework.views import APIView
from products.models import Product
from rest_framework import status
from rest_framework.response import Response
from products.serializers import ProductSerializer


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
    def post(self, request, course_id=''):
        try:
            course = CourseLink.objects.get(id=course_id)
            product_id = request.data['product_id']
            product = Product.objects.get(product_id)

            product.course_links.add(course)
            product.save()

            return Response(ProductSerializer(product).data, status=status.HTTP_200_OK)
        except (CourseLink.DoesNotExist, Product.DoesNotExist):
            return Response({'detail': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
