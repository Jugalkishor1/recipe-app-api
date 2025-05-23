"""
Test for models
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_Create_user_with_email_successfully(self):
        """ Test create user with email successfully """
        email = "test@example.com"
        password = "Test@1234"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test email is normalized for new users """
        sample_emails = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["Test2@Example.com", "Test2@example.com"],
            ["TEST3@EXAMPLE.COM", "TEST3@example.com"],
            ["test4@example.COM", "test4@example.com"]
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, "Test@1234")
            self.assertEqual(user.email, expected)

    def test_new_user_wihtout_email_raises_error(self):
        """ Test Creating a new user without email raises an ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', "Test@1234")

    def test_create_super(self):
        """ Test creating a superuser. """
        user = get_user_model().objects.create_superuser(
            "test@example.com", "Test@1234"
            )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
