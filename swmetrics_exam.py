import unittest
from math_test import wrapper


class Tests(unittest.TestCase):

    def test_wrapper_correct_args(self):
        self.assertEqual(wrapper(3), 6)


if __name__ == '__main__':
    unittest.main()