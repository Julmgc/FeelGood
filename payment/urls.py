from django.urls import path

from payment.views import ListCreatePayment, RetrieveRemovePayment


urlpatterns = [
    path('payment/', ListCreatePayment.as_view()),
    path('payment/<paymentId>/', RetrieveRemovePayment.as_view()),
]
