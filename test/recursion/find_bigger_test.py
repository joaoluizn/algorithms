from unittest import TestCase
from src.recursion.find_bigger import find_bigger

class CountListTests(TestCase):

    def test_find_bigger_from_empty_list(self):
        values = []
        self.assertEqual(find_bigger(values), 0)

    def test_find_bigger_from_single_item_list(self):
        values = [6]
        self.assertEqual(find_bigger(values), 6)

    def test_find_bigger_from_list(self):
        values = [6, 4, 12, 2]
        self.assertEqual(find_bigger(values), 12)

    def test_find_bigger_from_ordered_list(self):
        values = [2, 4, 6, 12]
        self.assertEqual(find_bigger(values), 12)

    def test_find_bigger_from_ordered_list_with_negative(self):
        values = [-1, 4, 6, 12]
        self.assertEqual(find_bigger(values), 12)

    def test_find_bigger_from_reverse_order(self):
        values = [12, 7, 5, 1]
        self.assertEqual(find_bigger(values), 12)
