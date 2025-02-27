from django.test import TestCase

from django.urls import reverse


class IndexViewTests(TestCase):
    def test_returns_200(self):
        response = self.client.get(reverse("course_surveys:index"))

        self.assertEqual(response.status_code, 200)
