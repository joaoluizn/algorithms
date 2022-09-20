from unittest import TestCase, main
from src.recursion.binary_serach import binary_search

class BinarySearchRecursionTest(TestCase):

    def test_should_return_none_when_empty_list(self):
        self.assertIsNone(binary_search([], 1))

    def test_value_is_not_present(self):
        self.assertIsNone(binary_search(range(1, 7), 7))

    def test_value_is_present(self):
        self.assertEqual(binary_search(range(1, 9), 8), 8)

    def test_value_is_present_more_values(self):
        self.assertEqual(binary_search(range(1, 101), 100), 100)
