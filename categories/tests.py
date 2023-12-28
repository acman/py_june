from django.test import TestCase
from django.urls import reverse

from categories.models import MainCategory


class CategoryListViewTest(TestCase):
    def setUp(self):
        # Create some MainCategory instances for testing
        self.category1 = MainCategory.objects.create(name="Category 1")
        self.category2 = MainCategory.objects.create(name="Category 2")

    def test_category_list(self):
        response = self.client.get(reverse("categories:list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Category 1")
