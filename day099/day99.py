# simple_functions.py

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


# test_simple_functions.py

import unittest
# from simple_functions import add, multiply

class TestSimpleFunctions(unittest.TestCase):
    def test_add(self):
        # Test addition with positive numbers
        self.assertEqual(add(2, 3), 5)
        # Test addition with negative numbers
        self.assertEqual(add(-1, -1), -2)
        # Test addition with zero
        self.assertEqual(add(0, 5), 5)

    def test_multiply(self):
        # Test multiplication with positive numbers
        self.assertEqual(multiply(2, 3), 6)
        # Test multiplication with zero
        self.assertEqual(multiply(0, 10), 0)
        # Test multiplication with negative numbers
        self.assertEqual(multiply(-2, 3), -6)

if __name__ == '__main__':
    unittest.main()
