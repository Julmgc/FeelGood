from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from category.permissions import CanCreateCategory, CanGetCategory
from . models import Category
from . serializers import CategorySerializer
from rest_framework.authentication import TokenAuthentication

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
