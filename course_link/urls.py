from django.urls import path
from .views import CourseLinkCreateAndList, CourseLinkUpdateAndListOne, CourseAndProdut

urlpatterns = [
    path('course/', CourseLinkCreateAndList.as_view()),
    path('course/<str:course_id>/', CourseLinkUpdateAndListOne.as_view()),
    path('course/<str:courseId>/add/', CourseAndProdut.as_view()),
]
