from django.urls import path

from .views import UserView, LoginView, UserListOneView

urlpatterns = [
    path('register/', UserView.as_view()),
    path('login/', LoginView.as_view()),
    path('register/<str:user_id>/', UserListOneView.as_view()),
]
