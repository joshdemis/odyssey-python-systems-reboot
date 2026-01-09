import unittest

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


class TestMath(unittest.TestCase):

    def test_divide_success(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == "__main__":
    unittest.main()
