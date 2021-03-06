from django.urls import path

from product_reviews.views import ProductReviewListCreateView, ProductReviewIdView

urlpatterns = [
    path('productReview/', ProductReviewListCreateView.as_view()),
    path('productReview/<productReviewId>/', ProductReviewIdView.as_view()),
]
