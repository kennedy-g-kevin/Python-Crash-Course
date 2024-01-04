import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py"""

    def test_first_last_name(self):
        """Do names like Bob Smith work?"""
        formatted_name = get_formatted_name('bob', 'smith')
        self.assertEqual(formatted_name, 'Bob Smith')

    def test_first_last_middle_name(self):
        """Do names like Bob John Smith work?"""
        formatted_name = get_formatted_name('bob', 'smith', 'john')
        self.assertEqual(formatted_name, 'Bob John Smith')


if __name__ == '__main__':
    unittest.main()