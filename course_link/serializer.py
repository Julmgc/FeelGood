from rest_framework import serializers
from .models import CourseLink

class CourseLinkSerializer(serializers.ModelSerializer):
    link = serializers.URLField()
    
    class Meta:
        model = CourseLink
        fields = ['id','link']
        