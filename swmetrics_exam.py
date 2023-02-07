"""Exam"""

import unittest
from math_test import wrapper

class Tests(unittest.TestCase):
    """Test cases"""
    def test_wrapper_correct_args(self):
        """Correct Inputs"""
        self.assertEqual(wrapper(3), 6)
    def test_wrapper_incorrect_args(self):
        """Incorrect Inputs"""
        with self.assertRaises(TypeError):
            wrapper("three")
    def test_wrapper_negative_args(self):
        """Factorial input can't be negative"""
        with self.assertRaises(TypeError):
            wrapper("-3")
    def test_wrapper_without_args(self):
        """Input needed"""
        with self.assertRaises(TypeError):
            wrapper("")

if __name__ == '__main__':
    unittest.main()
