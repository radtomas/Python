"""
Radoslaw Tomaszewski
poczta@radtomas.pl
"""


def binarySearch(array, l, r, x):
    """
    Search function using binary search algorithm.(Recursive)
    array - sorted array
    l - left index(in python 0)
    r - right index(len(array))
    x - value of index search
    """
    if r >= l:

        # calculate mid of array
        mid = (l + r) // 2

        if array[mid] == x:
            return mid

        # if mid is bigger then reduce section with mid as rigt border
        elif array[mid] > x:
            return binarySearch(array, l, mid, x)
        # elif mid is smaller then reduce section with mid as left border
        elif array[mid] < x:
            return binarySearch(array, mid, r, x)

    else:
        return -1


def binarySearchB(array, l, r, x):
    """
    Search function using binary search algorithm.
    array - sorted array
    l - left index(in python 0)
    r - right index(len(array))
    x - value of index search
    """
    if r >= l:
        while r > l:
            mid = (r + l) // 2

            if array[mid] < x:
                l = mid + 1
            else:
                r = mid
        if array[r] == x:
            return r
    else:
        return -1


def main():
    array = [1, 3, 5, 7, 9, 22, 45, 55, 57, 200, 323, 432, 535]

    for i in array:
        print("A", i, binarySearch(array, 0, len(array), i))
        print("B", i, binarySearchB(array, 0, len(array), i))


if __name__ == "__main__":
    main()
