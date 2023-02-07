import unittest
from math_test import wrapper


class Tests(unittest.TestCase):

    def test_wrapper_correct_args(self):
        self.assertEqual(wrapper(3), 6)

    def test_wrapper_incorrect_args(self):
        with self.assertRaises(TypeError):
            wrapper("three", 6)

    def test_wrapper_negative_args(self):
        with self.assertRaises(TypeError):
            wrapper("-3", 6)


if __name__ == '__main__':
    unittest.main()