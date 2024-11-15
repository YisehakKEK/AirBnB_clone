import unittest
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel
from models import storage
from models.user import User
from console import HBNBCommand

class TestConsole(unittest.TestCase):

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            output = f.getvalue().strip()
            # Check if the output is a valid UUID (id)
            self.assertTrue(len(output) > 0)
            self.assertTrue(output.isalnum())

    def test_show(self):
        # First, create a User
        user = User()
        user.save()
        user_id = user.id
        
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User {user_id}")
            output = f.getvalue().strip()
            self.assertIn(user_id, output)
            self.assertIn("User", output)
        
        # Show with invalid ID
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User fake_id")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")
    
    def test_destroy(self):
        # Create and destroy a user instance
        user = User()
        user.save()
        user_id = user.id
        
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy User {user_id}")
            output = f.getvalue().strip()
            self.assertEqual(output, "")
        
        # Try to destroy with invalid ID
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy User fake_id")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_all(self):
        # Create a few users
        user1 = User()
        user2 = User()
        user1.save()
        user2.save()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            output = f.getvalue().strip()
            self.assertIn("User", output)
            self.assertIn(user1.id, output)
            self.assertIn(user2.id, output)
        
        # Test all command without class name
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            output = f.getvalue().strip()
            self.assertIn("User", output)
            self.assertIn("State", output)  # Example: Assuming State class is used
            self.assertIn("City", output)   # Example: Assuming City class is used

    def test_count(self):
        # Create users and check count
        user1 = User()
        user2 = User()
        user1.save()
        user2.save()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count User")
            output = f.getvalue().strip()
            self.assertEqual(output, "2")
        
        # Test count with invalid class name
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count FakeClass")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_update(self):
        # Create a user instance and update it
        user = User()
        user.save()
        user_id = user.id
        
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {user_id} first_name John")
            output = f.getvalue().strip()
            self.assertEqual(output, "")
        
        # Verify the update
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User {user_id}")
            output = f.getvalue().strip()
            self.assertIn("first_name", output)
            self.assertIn("John", output)

    def test_update_from_dict(self):
        # Create a user and update using a dictionary
        user = User()
        user.save()
        user_id = user.id
        
        update_dict = '{"first_name": "Alice", "last_name": "Smith"}'
        
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {user_id} {update_dict}")
            output = f.getvalue().strip()
            self.assertEqual(output, "")
        
        # Verify the update
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User {user_id}")
            output = f.getvalue().strip()
            self.assertIn("first_name", output)
            self.assertIn("Alice", output)
            self.assertIn("last_name", output)
            self.assertIn("Smith", output)

    def test_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            output = f.getvalue().strip()
            self.assertIn("show", output)
            self.assertIn("Prints", output)

if __name__ == '__main__':
    unittest.main()
