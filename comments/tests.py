from django.test import TestCase
from django.urls import reverse

from comments.forms import CommentForm
from comments.models import Comment
from core.tests import TestDataMixin


class CreateCommentTest(TestDataMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.create_comment_url = reverse(
            "comments:create", kwargs={"post_slug": self.post.slug}
        )

    def test_create_comment_view_get(self):
        self.client.force_login(self.user)

        response = self.client.get(self.create_comment_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "comments/comment_form.html")
        self.assertIsInstance(response.context["form"], CommentForm)
        self.assertEqual(response.context["post"], self.post)

    def test_create_comment_view_post(self):
        self.client.force_login(self.user)

        data = {
            "title": "Test Comment1",
            "content": "Rest comment content1",
        }

        response = self.client.post(self.create_comment_url, data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            reverse(
                "categories:detail", kwargs={"category_slug": self.post.category.slug}
            ),
        )

        comment = Comment.objects.get(title="Test Comment1")
        self.assertEqual(comment.title, "Test Comment1")
        self.assertEqual(comment.post, self.post)
