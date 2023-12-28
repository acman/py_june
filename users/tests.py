from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


class SignUpViewTest(TestCase):
    def setUp(self):
        # Test client
        # self.client = Client()

        # URL for view
        self.signup_url = reverse("users:signup")

        # Cleanup test db
        get_user_model().objects.all().delete()

    def test_signup_view_get(self):
        # Check GET request
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/signup.html")

    def test_signup_view_post_valid_data(self):
        # Check POST request with correct data
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "password1": "testpassword123",
            "password2": "testpassword123",
        }
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))

        # Check that user in db
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertTrue(get_user_model().objects.filter(username="testuser").exists())

    def test_signup_view_post_invalid_data(self):
        # Check POST request with invalid data
        data = {
            "username": "testuser",
            "email": "invalidemail",
            "password1": "testpassword123",
            "password2": "testpassword123",
        }
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/signup.html")

        # Check that user are not on db
        self.assertEqual(get_user_model().objects.count(), 0)


class LogInViewTest(TestCase):
    def setUp(self):
        # Test client
        # self.client = Client()

        # URL for view
        self.login_url = reverse("users:login")

    def test_login_view_get(self):
        # Check GET request
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/login.html")

    def test_login_view_post_valid_data(self):
        # Check POST request with correct data
        user = get_user_model().objects.create_user(
            username="testuser",
            password="testpassword123",
        )

        data = {
            "username": "testuser",
            "password": "testpassword123",
        }
        response = self.client.post(self.login_url, data, follow=True)

        self.assertRedirects(response, reverse("home"))
        self.assertTrue(response.context["user"].is_authenticated)

    def test_login_view_post_invalid_data(self):
        # Check POST request with invalid data
        data = {
            "username": "nonexistentuser",
            "password": "testpassword123",
        }
        response = self.client.post(self.login_url, data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/login.html")
        self.assertContains(response, "Please enter a correct username and password")

    def test_login_view_post_no_data(self):
        response = self.client.post(self.login_url, {})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/login.html")
