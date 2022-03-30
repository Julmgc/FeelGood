from django.urls import path
from .views import InvoiceGetView, InvoiceGetOneView, InvoiceGetOneTransactionView

urlpatterns = [
    path('invoice/', InvoiceGetView.as_view()),
    path('invoice/<str:invoice_id>/', InvoiceGetOneView.as_view()),
    path('invoice/transaction/<str:transaction_id>/',
         InvoiceGetOneTransactionView.as_view())
]
