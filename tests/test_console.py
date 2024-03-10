#!/usrbin/python3
"""Module contains tests for console.py"""

# import console
from console import HBNBCommand
import unittest


class TestConsole(unittest.TestCase):
    """Inherits from unittest,testcase"""
    def create_interpreter(self):
        """Creates interpreter itself"""
        return HBNBCommand()

    def test_quit(self):
        """Tests for the method do_quit"""
        d_console = self.create_interpreter()
        self.assertTrue(d_console.onecmd("quit"))

    def test_EOF(self):
        """Tests for the method do_EOF"""
        d_console = self.create_interpreter()
        self.assertTrue(d_console.onecmd("EOF"))


if __name__ == "__main__":
    unittest.main()
