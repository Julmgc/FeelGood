from django.urls import path
from .views import CourseLinkCreateAndList,CourseLinkUpdateAndListOne,CourseAndProduto

urlpatterns =[ 
    path('course/',CourseLinkCreateAndList.as_view()),
    path('course/<str:course_id>/',CourseLinkUpdateAndListOne.as_view()), 
    path('course/<str:course_id>/',CourseAndProduto.as_view()), 
]