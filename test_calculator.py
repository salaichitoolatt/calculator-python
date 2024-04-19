import unittest
from calculator import multiply_numbers

class TestMultiply(unittest.TestCase):
    def test_positive_numbers(self):
        result = multiply_numbers(5, 7)
        self.assertEqual(result, 35)

    def test_negative_numbers(self):
        result = multiply_numbers(-5, -7)
        self.assertEqual(result, 35)

    def test_mixed_numbers(self):
        result = multiply_numbers(5, -7)
        self.assertEqual(result, -35)

    def test_zero(self):
        result = multiply_numbers(0, 7)
        self.assertEqual(result, 0)

    def test_decimal_numbers(self):
        result = multiply_numbers(3.5, 2)
        self.assertEqual(result, 7)

if __name__ == '__main__':
    unittest.main()
