from unittest import TestCase
from src.binary_search import binary_search

class BinarySearchTest(TestCase):

    def test_should_return_none_when_empty_list(self):
        self.assertIsNone(binary_search([], 1))

    def test_value_is_not_present(self):
        self.assertIsNone(binary_search(range(1, 7), 7))

    def test_value_is_present(self):
        self.assertEqual(binary_search(range(1,101), 100), 99)
