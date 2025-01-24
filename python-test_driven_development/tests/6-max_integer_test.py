import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittests for the max_integer function"""

    def test_positive_integers(self):
        """Test with a list of positive integers"""
        self.assertEqual(max_integer([45, 2, 78, 90]), 90)

    def test_negative_integers(self):
        """Test with a list of negative integers"""
        self.assertEqual(max_integer([-12, -45, -67, -3]), -3)

    def test_single_integer(self):
        """Test with a single integer in the list"""
        self.assertEqual(max_integer([1]), 1)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_mixed_values(self):
        """Test with mixed positive and negative integers"""
        self.assertEqual(max_integer([10, -20, 50, -10]), 50)

    def test_repeated_elements(self):
        """Test with repeated values in the list"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_large_numbers(self):
        """Test with large numbers in the list"""
        self.assertEqual(max_integer([123456789, 987654321, 555555555]), 987654321)

    def test_floats_in_list(self):
        """Test with floating point numbers"""
        self.assertEqual(max_integer([1.25, 3.14, 2.71]), 3.14)

    def test_floats_and_integers(self):
        """Test with a mix of integers and floating point numbers"""
        self.assertEqual(max_integer([1, 2.5, 0.5, 7]), 7)

    def test_string_values(self):
        """Test with a list of strings"""
        self.assertEqual(max_integer(["Jus", "Eau", "Café", "Sirop"]), "Sirop")

    def test_mixed_strings_and_numbers(self):
        """Test with mixed strings and numbers (unsupported type)"""
        with self.assertRaises(TypeError):
            max_integer([1, "Sirop", 3.5])

    def test_invalid_type(self):
        """Test with a non-iterable argument"""
        with self.assertRaises(TypeError):
            max_integer(100)

if __name__ == "__main__":
    unittest.main()