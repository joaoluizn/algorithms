from unittest import TestCase
from src.recursion.count_list import count_elements

class CountListTests(TestCase):

    def test_count_of_empty_list(self):
        values = []
        self.assertEqual(count_elements(values), 0)

    def test_count_of_single_item_list(self):
        values = [1]
        self.assertEqual(count_elements(values), 1)

    def test_count_list(self):
        values = [1,2,3,4]
        self.assertEqual(count_elements(values), 4)

    def test_count_list_more_elements(self):
        values = [1,2,3,5,6,7]
        self.assertEqual(count_elements(values), 6)

