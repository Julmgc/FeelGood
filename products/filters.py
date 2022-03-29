import django_filters

from products.models import Product


class ProductFilter(django_filters.FilterSet):
    categories = django_filters.CharFilter(
        field_name='categories__name',
        lookup_expr='contains',
    )

    class Meta:
        model = Product
        fields = ['categories__name', 'name', 'price_client', "price_seller"]
