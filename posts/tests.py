from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from categories.models import Category, MainCategory
from posts.models import Post


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


class DetailsPostViewTest(TestCase):
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

        self.post = Post.objects.create(
            title="Test Post",
            content="Test content",
            author=self.user,
            category=self.category,
            created_at="2023-01-01T00:00:00Z",
            updated_at="2023-01-01T00:00:00Z",
            is_active=True,
        )

        self.detail_post_view_url = reverse(
            "posts:details", kwargs={"post_id": self.post.pk}
        )

    def test_detail_post_view(self):
        response = self.client.get(self.detail_post_view_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/post_detail.html")
        self.assertEqual(response.context["post"], self.post)

    def test_detail_post_view_404(self):
        self.post.is_active = False
        self.post.save()

        response = self.client.get(self.detail_post_view_url)

        self.assertEqual(response.status_code, 404)
