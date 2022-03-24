from django.test import TestCase
from course_link.models import CourseLink

class TestCourseLinkModel(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.link = 'http/algoassim.com'

        cls.course_link = CourseLink.objects.create(
            link = cls.link
        )

    def test_course_link_field(self):
        self.assertIsInstance(self.course_link.link, str)
        self.assertEqual(self.course_link.link, self.link)
