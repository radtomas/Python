"""
Radoslaw Tomaszewski
poczta@radtomas.pl
"""


def merge(left_array, right_array):
    """
    Merge function which merge two subarrays
    left_array - left piece of main array
    right_array - right piece of main array
    """

    # temp array
    temp_array = []

    while len(left_array) != 0 and len(right_array) != 0:
        if left_array[0] < right_array[0]:
            temp_array.append(left_array[0])
            left_array.remove(left_array[0])
        else:
            temp_array.append(right_array[0])
            right_array.remove(right_array[0])

    if len(left_array) == 0:
        temp_array += right_array
    else:
        temp_array += left_array

    return temp_array


def merge_sort(array):
    """
    Sort function using merge sort algorithm.
    array - unsorted array
    """

    if len(array) > 1:
        mid = len(array) // 2

        # Sort left and right halves
        left_array = merge_sort(array[:mid])
        right_array = merge_sort(array[mid:])
        return merge(left_array, right_array)
    else:
        return array


def main():
    array = [10, 7, 8, 9, 1, 5, 34, 222, 1232, 6]

    print("Starting array:", array)
    print("Sorted array:", merge_sort(array))


if __name__ == "__main__":
    main()
