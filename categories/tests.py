from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from categories.models import Category, MainCategory
from posts.models import Post


class CategoryModelTest(TestCase):
    def setUp(self):
        self.main_category = MainCategory.objects.create(title="MainCategory")
        self.category = Category(
            title="Українська категорія",
            description="Test description",
            main_category=self.main_category,
        )
        # It is required to create slug
        self.category.save()

    def test_category_model(self):
        self.assertEqual(self.category.title, "Українська категорія")
        self.assertEqual(self.category.slug, "ukrayinska-kategoriia")
        self.assertEqual(self.category.description, "Test description")
        self.assertEqual(self.category.main_category.title, "MainCategory")

    def test_category_model_str(self):
        self.assertEqual(str(self.category), "Українська категорія")


class CategoryListViewTest(TestCase):
    def setUp(self):
        # Create some MainCategory instances for testing
        self.category1 = MainCategory.objects.create(title="Category 1")
        self.category2 = MainCategory.objects.create(title="Category 2")

    def test_category_list(self):
        response = self.client.get(reverse("categories:list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Category 1")


class CategoryDetailViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpassword123",
        )
        self.main_category = MainCategory.objects.create(title="MainCategory")
        self.category = Category.objects.create(
            title="Test category",
            description="Test description",
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

    def test_category_detail(self):
        response = self.client.get(
            reverse("categories:detail", kwargs={"category_id": self.category.pk})
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")
