from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from categories.models import Category, MainCategory


class CreatePostViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpassword123",
        )

        self.main_category = MainCategory.objects.create(
            name="MainCategory",
        )

        self.category = Category.objects.create(
            name="Test Category",
            main_category=self.main_category,
        )

        self.create_view_url = reverse(
            "posts:create", kwargs={"category_id": self.category.pk}
        )

    def test_create_post_view_get(self):
        self.client.force_login(self.user)
        response = self.client.get(self.create_view_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/post_form.html")

    def test_create_post_view_post(self):
        self.client.force_login(self.user)

        data = {
            "title": "test title",
            "content": "Test text",
        }

        response = self.client.post(self.create_view_url, data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("categories:list"))
        self.assertEqual(self.category.post_set.count(), 1)

    def test_create_post_view_post_invalid_data(self):
        self.client.force_login(self.user)

        data = {}

        response = self.client.post(self.create_view_url, data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/post_form.html")
        self.assertEqual(self.category.post_set.count(), 0)
