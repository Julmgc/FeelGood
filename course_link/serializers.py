from rest_framework import serializers

from course_link.models import CourseLink


class CourseLinkSerializer(serializers.ModelSerializer):
    link = serializers.URLField()

    class Meta:
        model = CourseLink
        fields = '__all__'
