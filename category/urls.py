from django.urls import path
from . views import CategoryViews, SpecificCategoryViews
urlpatterns = [
    path('category/', CategoryViews.as_view()),
    path('category/<str:category_id>/', SpecificCategoryViews.as_view()),
]