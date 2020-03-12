"""
Radoslaw Tomaszewski
poczta@radtomas.pl
"""


def _merge(left_array, right_array):
    """
    Merge function which merge two subarrays
    left_array - left piece of main array
    right_array - right piece of main array
    """
    temp_array = []
    right_len = len(right_array)
    left_len = len(left_array)

    while left_len != 0 and right_len != 0:
        if left_array[0] < right_array[0]:
            temp_array.append(left_array[0])
            left_array.remove(left_array[0])
        else:
            temp_array.append(right_array[0])
            right_array.remove(right_array[0])

    if left_len == 0:
        temp_array += right_array
    else:
        temp_array += left_array

    return temp_array


def merge_sort(array):
    """
    Sort function using merge sort algorithm.
    array - unsorted array
    """
    array_len = len(array)

    if array_len > 1:
        mid = array_len // 2

        # Sort left and right halves
        left_array = merge_sort(array[:mid])
        right_array = merge_sort(array[mid:])
        return _merge(left_array, right_array)
    else:
        return array


def main():
    array = [10, 7, 8, 9, 1, 5, 34, 222, 1232, 6]

    print("Starting array:", array)
    print("Sorted array:", merge_sort(array))


if __name__ == "__main__":
    main()
