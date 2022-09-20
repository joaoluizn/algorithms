from unittest import TestCase
from src.recursion.sum_list import sum_list

class SumListTests(TestCase):

    def test_sum_of_empty_list(self):
        values = []
        self.assertEqual(sum_list(values), 0)

    def test_sum_of_single_item_list(self):
        values = [1]
        self.assertEqual(sum_list(values), 1)

    def test_sum_list(self):
        values = [1,2,3,4]
        self.assertEqual(sum_list(values), 10)

    def test_sum_list_2(self):
        values = [1,2,3,5,6,7]
        self.assertEqual(sum_list(values), 24)

