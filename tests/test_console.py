#!/usr/bin/env python3
"""
Unittest for console module
"""
import unittest
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """Test cases for HBNBCommand console."""

    def setUp(self):
        """Set up shared resources."""
        self.cli = HBNBCommand()

    def test_docstrings(self):
        """Test that all docstrings are present."""
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(self.cli.do_create.__doc__)
        self.assertIsNotNone(self.cli.do_show.__doc__)

    def _run_command(self, command):
        """Helper to run a command and capture output."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.onecmd(command)
            return fake_out.getvalue()

    def test_empty_line(self):
        """Empty input should do nothing (no output)."""
        output = self._run_command('
')
        self.assertEqual(output, '')

    def test_quit(self):
        """Quit command should exit the loop."""
        with self.assertRaises(SystemExit):
            self.cli.onecmd('quit')

    def test_EOF(self):
        """EOF command should exit with a newline and SystemExit."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with self.assertRaises(SystemExit):
                self.cli.onecmd('EOF')
            self.assertEqual(fake_out.getvalue(), '
')

    def test_create_missing_class(self):
        """create with no class should print error."""
        output = self._run_command('create')
        self.assertIn('** class name missing **', output)

    def test_create_unknown_class(self):
        """create with invalid class should print error."""
        output = self._run_command('create Unknown')
        self.assertIn("** class doesn't exist **", output)

    def test_show_missing_class(self):
        """show with no args prints missing class msg."""
        output = self._run_command('show')
        self.assertIn('** class name missing **', output)

    def test_show_unknown_class(self):
        output = self._run_command('show Unknown')
        self.assertIn("** class doesn't exist **", output)

    def test_show_missing_id(self):
        output = self._run_command('show BaseModel')
        self.assertIn('** instance id missing **', output)

    def test_show_no_instance(self):
        output = self._run_command('show BaseModel 1234-5678')
        self.assertIn('** no instance found **', output)

    def test_all_no_class(self):
        """all with no class prints all objects (at least [] string)."""
        output = self._run_command('all')
        self.assertTrue(output.startswith('['))

    def test_all_unknown_class(self):
        output = self._run_command('all Unknown')
        self.assertIn("** class doesn't exist **", output)

    def test_update_missing_args(self):
        output = self._run_command('update')
        self.assertIn('** class name missing **', output)

    def test_count(self):
        """count should return number of instances for a class."""
        # Ensure at least zero count
        output = self._run_command('count BaseModel')
        # Should be numeric
        self.assertTrue(output.strip().isdigit())


if __name__ == '__main__':
    unittest.main()
