from django.test import TestCase
from django.urls import reverse


class HomePageTest(TestCase):
    def test_home_page_get_success(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
