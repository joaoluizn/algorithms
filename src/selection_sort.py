""" 
Here we have a simple Selection Sort implementation.

1 - Get smallest value from array
2 - Add it to the new array
3 - Return the sorted array

- Time Complexity: BigO(N^2)
"""


def selection_sort(array):
    sorted_array = []
    for _ in range(0, len(array)):
        major_index = find_smallest(array)
        sorted_array.append(array.pop(major_index))
    return sorted_array


def find_smallest(array):
    index = 0
    minor = array[index]
    for curr_index, value in enumerate(array):
        if value < minor:
            minor = value
            index = curr_index
    return index
