from rest_framework import serializers
from transactions.exceptions import TransactionError
from category.models import Category
from course_link.models import CourseLink
from products.models import Product
from category.serializers import CategorySerializer
from course_link.serializers import CourseLinkSerializer
from sales.models import Sale
from rest_framework.exceptions import ValidationError

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
        depth = 1
        extra_kwargs = {
            'is_active': {'required': False},
            'course_links': {'required': False, 'read_only': True},
            'categories': {'required': False, 'read_only': True},
        }

    def create(self, validated_data):
        new_course_links = self.context['view'].request.data.get('course_links', [])
        new_categories = self.context['view'].request.data.get('categories', [])

        for link in new_course_links:
            serialized = CourseLinkSerializer(data={'link': link})
            serialized.is_valid(raise_exception=True)
        for name in new_categories:
            serialized = CategorySerializer(data={'name': name})
            serialized.is_valid(raise_exception=True)

        new_product = Product.objects.create(**validated_data)

        for course in new_course_links:
            serialized = CourseLinkSerializer(data={'link': course})
            serialized.is_valid(raise_exception=True)

            new_course = CourseLink.objects.get_or_create(**serialized.validated_data)[0]
            new_product.course_links.add(new_course)

        for category in new_categories:
            serialized = CategorySerializer(data={'name': category})
            serialized.is_valid(raise_exception=True)

            new_category = Category.objects.get_or_create(**serialized.validated_data)[0]
            new_product.categories.add(new_category)

        return new_product

    def update(self, instance, validated_data):
        sale = self.context['view'].request.data.get(
            'sale', None)
        if sale is not None:
            founded_sale = Sale.objects.get(id=sale)
            if not founded_sale:
                raise ValidationError(
                {"detail": "Sale was not found"})
            instance.sale.add(founded_sale)


        new_course_links = self.context['view'].request.data.get(
            'course_links', [])
        new_categories = self.context['view'].request.data.get(
            'categories', [])

        for link in new_course_links:
            serialized = CourseLinkSerializer(data={'link': link})
            serialized.is_valid(raise_exception=True)
        for name in new_categories:
            serialized = CategorySerializer(data={'name': name})
            serialized.is_valid(raise_exception=True)

        if self.context['view'].request.method == "PUT":
            instance.course_links.clear()
            instance.categories.clear()

        for course in new_course_links:
            serialized = CourseLinkSerializer(data={'link': course})
            serialized.is_valid(raise_exception=True)

            new_course = CourseLink.objects.get_or_create(
                **serialized.validated_data)[0]
            instance.course_links.add(new_course)

        for category in new_categories:
            serialized = CategorySerializer(data={'name': category})
            serialized.is_valid(raise_exception=True)

            new_category = Category.objects.get_or_create(
                **serialized.validated_data)[0]
            instance.categories.add(new_category)

        return super().update(instance, validated_data)


class ProductsTransactionsSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    quantity = serializers.IntegerField(min_value=0)

    def validate(self, attrs):
        try:
            product = Product.objects.get(id=attrs["id"])
        except Product.DoesNotExist:
            raise TransactionError({"detail": "Product not found"}, code=404)

        if product.quantity < attrs["quantity"]:
            raise TransactionError({"detail": f'Product {product.name} quantity is not enough'}, code=400)

        return super().validate(attrs)
