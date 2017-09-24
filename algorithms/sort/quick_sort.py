"""
Radoslaw Tomaszewski
poczta@radtomas.pl
"""


def quickSort(array):
    """
    Sort function using quick sort algorithm.
    array - unsorted array
    """
    if len(array) <= 1:
        return array

    pivot = array[0]

    # Separation element on less, equal, greater than pivot
    less = [i for i in array if i < pivot]
    equal = [i for i in array if i == pivot]
    greater = [i for i in array if i > pivot]

    return quickSort(less) + equal + quickSort(greater)


def main():
    array = [10, 7, 8, 9, 1, 5]

    print(quickSort(array))


if __name__ == "__main__":
    main()
