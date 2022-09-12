from unittest import TestCase
from src.selection_sort import find_smallest, selection_sort

class SelectionSortTest(TestCase):
    
    def test_find_smallest_in_array(self):
        target_array = [40, 60, 20]
        smallest_index = find_smallest(target_array)
        self.assertEqual(target_array[smallest_index], 20)

    def test_sort_with_selection_sort(self):
        target_array = [40, 60, 15, 20]
        sorted_array = selection_sort(target_array)
        self.assertEqual(sorted_array, [15, 20, 40, 60])
