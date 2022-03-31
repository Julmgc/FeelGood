from django.urls import path

from sales.views import SaleListCreateView, SaleIdView


urlpatterns = [
    path("sale/", SaleListCreateView.as_view()),
    path("sale/<sale_id>/", SaleIdView.as_view()),

]
