from django.urls import path

from . views import CategoryViews, SpecificCategoryViews, CategoryAndProdutView

urlpatterns = [
    path('category/', CategoryViews.as_view()),
    path('category/<str:category_id>/', SpecificCategoryViews.as_view()),
    path('category/product/<str:category_id>/', CategoryAndProdutView.as_view()),

]
