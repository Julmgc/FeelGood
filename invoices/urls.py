from django.urls import path
from .views import InvoiceGetView, InvoiceGetOneView

urlpatterns = [
    path('invoice/', InvoiceGetView.as_view()),
    path('invoice/<str:invoice_id>/', InvoiceGetOneView.as_view()),

]
