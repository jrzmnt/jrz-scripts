"""
Sorts an array in ascending order using the Merge Sort algorithm.

Parameters:
- array (list): The list of elements to be sorted. The list is modified in place.

Returns:
- None: The array is sorted in place, so no value is returned.

Algorithm:
1. Divide the array into two halves.
2. Recursively sort each half.
3. Merge the two sorted halves back together in ascending order.

Example:
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    merge_sort(numbers)
    # numbers will be [1, 2, 4, 5, 6, 8, 10, 14]
"""


def merge_sort(array):
    if len(array) <= 1:
        return

    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    merge_sort(left_part)
    merge_sort(right_part)

    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1

    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1


if __name__ == "__main__":
    numbers = [4, 10, 6, 14, 2, 1, 8, 5, 200, 2, 2, 11, 12, 13, 1, 1, 9, 0]
    print(f"Unsorted array: {numbers}")
    merge_sort(numbers)
    print(f"Sorted array: {numbers}")
