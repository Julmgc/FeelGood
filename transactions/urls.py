from django.urls import path

from transactions.views import ListCreateTransaction, RetrieveTransaction


urlpatterns = [
    path('transaction/', ListCreateTransaction.as_view()),
    path('transaction/<str:transactionId>/', RetrieveTransaction.as_view()),
]
