#!/usrbin/python3
"""Module contains tests for console.py
"""

from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
import unittest


class TestHBNBCommand(unittest.TestCase):
    """Unittests for testing help messages of the HBNB command interpreter."""

    def test_quit(self):
        pass

    def test_EOF(self):
        pass

    def test_create(self):
        r = ("Usage: create <class>\n        "
             "Create a new class instance and print its id.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(r, output.getvalue().strip())

    def test_show(self):
        r = ("Usage: show <class> <id> or <class>.show(<id>)\n        "
             "Display the string representation of a class instance of"
             " a given id.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(r, output.getvalue().strip())

    def test_destroy(self):
        r = ("Usage: destroy <class> <id> or <class>.destroy(<id>)\n        "
             "Delete a class instance of a given id.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(r, output.getvalue().strip())

    def test_all(self):
        r = ("Usage: all or all <class> or <class>.all()\n        "
             "Display string representations of all instances of a given class"
             ".\n        If no class is specified, displays all instantiated "
             "objects.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(r, output.getvalue().strip())

    def test_count(self):
        r = ("Usage: count <class> or <class>.count()\n        "
             "Retrieve the number of instances of a given class.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(r, output.getvalue().strip())

    def test_update(self):
        r = ("Usage: update <class> <id> <attribute_name> <attribute_value> or"
             "\n       <class>.update(<id>, <attribute_name>, <attribute_value"
             ">) or\n       <class>.update(<id>, <dictionary>)\n        "
             "Update a class instance of a given id by adding or updating\n   "
             "     a given attribute key/value pair or dictionary.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(r, output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
