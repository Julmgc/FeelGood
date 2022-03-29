from django.urls import path

from products.views import ListCreateProduct, RetrieveUpdateDestroyProduct


urlpatterns = [
    path('products/', ListCreateProduct.as_view()),
    path('products/<str:productId>/', RetrieveUpdateDestroyProduct.as_view()),
]
