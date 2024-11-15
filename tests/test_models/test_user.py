import unittest
from models.user import User

class TestUser(unittest.TestCase):

    def test_create_instance(self):
        """Test that an instance of User is created correctly."""
        user = User()
        self.assertIsInstance(user, User)

    def test_email(self):
        """Test that the email attribute is present in the User class."""
        user = User()
        user.email = "test@example.com"
        self.assertEqual(user.email, "test@example.com")

    def test_first_name(self):
        """Test that the first_name attribute is present in the User class."""
        user = User()
        user.first_name = "John"
        self.assertEqual(user.first_name, "John")

    def test_last_name(self):
        """Test that the last_name attribute is present in the User class."""
        user = User()
        user.last_name = "Doe"
        self.assertEqual(user.last_name, "Doe")