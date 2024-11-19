import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.user import User
from unittest.mock import patch, MagicMock


class TestHBNBCommand(unittest.TestCase):
    """Unit tests for the HBNBCommand console."""

    def setUp(self):
        """Setup resources before each test."""
        self.console = HBNBCommand()
        self.mock_storage = patch('models.storage').start()
        self.mock_storage.all.return_value = {}
        self.addCleanup(patch.stopall)

    def tearDown(self):
        """Clean up resources after each test."""
        storage._FileStorage__objects = {}

    def test_quit(self):
        """Test quit command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("quit")
            self.assertEqual(f.getvalue(), "")

    def test_EOF(self):
        """Test EOF command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("EOF")
            self.assertEqual(f.getvalue(), "\n")

    def test_emptyline(self):
        """Test empty line input."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("")
            self.assertEqual(f.getvalue(), "")

    def test_create(self):
        """Test create command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()
            self.assertTrue(user_id in storage.all().keys())

    def test_show(self):
        """Test show command."""
        obj = User()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show User {obj.id}")
            self.assertIn(obj.id, f.getvalue())

    def test_destroy(self):
        """Test destroy command."""
        obj = User()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"destroy User {obj.id}")
        self.assertNotIn(f"User.{obj.id}", storage.all())

    def test_all(self):
        """Test all command."""
        obj = User()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all User")
            self.assertIn(f"[User] ({obj.id})", f.getvalue())

    def test_update(self):
        """Test update command."""
        obj = User()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'update User {obj.id} first_name "John"')
            self.assertIn("Updated", f.getvalue())
        self.assertEqual(storage.all()[f"User.{obj.id}"].first_name, "John")

    def test_update_dict(self):
        """Test update command with a dictionary."""
        obj = User()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'update User {obj.id} {{"age": 30, "email": "test@example.com"}}')
        updated_obj = storage.all()[f"User.{obj.id}"]
        self.assertEqual(updated_obj.age, 30)
        self.assertEqual(updated_obj.email, "test@example.com")

    def test_count(self):
        """Test <class name>.count() command."""
        obj1 = User()
        obj2 = User()
        obj1.save()
        obj2.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.count()")
            self.assertEqual(int(f.getvalue().strip()), 2)

    def test_default_show(self):
        """Test <class name>.show(<id>) command."""
        obj = User()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"User.show({obj.id})")
            self.assertIn(obj.id, f.getvalue())

    def test_default_destroy(self):
        """Test <class name>.destroy(<id>) command."""
        obj = User()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"User.destroy({obj.id})")
        self.assertNotIn(f"User.{obj.id}", storage.all())

    def test_invalid_class(self):
        """Test invalid class commands."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create InvalidClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show_invalid_id(self):
        """Test show command with an invalid ID."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show User invalid_id")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")
    
    def test_default_advanced_update(self):
        """Test <class name>.update(<id>, <attribute dict>) command."""
        obj = User()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'User.update({obj.id}, {{"age": 25, "city": "New York"}})')
        updated_obj = storage.all()[f"User.{obj.id}"]
        self.assertEqual(updated_obj.age, 25)
        self.assertEqual(updated_obj.city, "New York")

    def test_all_no_arguments(self):
        """Test all command without arguments."""
        user = User()
        user.save()
        state = State()
        state.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
            output = f.getvalue()
            self.assertIn(f"[User] ({user.id})", output)
            self.assertIn(f"[State] ({state.id})", output)


if __name__ == "__main__":
    unittest.main()
