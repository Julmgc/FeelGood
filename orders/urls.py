from django.urls import path
from .views import OrderGetView,OrderGetOneView,OrderGetOneTransactionView

urlpatterns = [
    path('order/',OrderGetView.as_view()),
    path('order/<str:order_id>/',OrderGetOneView.as_view()),
    path('order/transaction/<str:transaction_id>/',OrderGetOneTransactionView.as_view())
]