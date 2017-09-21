"""
Radoslaw Tomaszewski
poczta@radtomas.pl
"""


def merge(leftArray, rightArray):
    """
    Merge function which merge two subarrays
    leftArray - left piece of main array
    rightArray - right piece of main array
    """

    # temp array
    tempArray = []

    while len(leftArray) != 0 and len(rightArray) != 0:
        if leftArray[0] < rightArray[0]:
            tempArray.append(leftArray[0])
            leftArray.remove(leftArray[0])
        else:
            tempArray.append(rightArray[0])
            rightArray.remove(rightArray[0])

    if len(leftArray) == 0:
        tempArray += rightArray
    else:
        tempArray += leftArray

    return tempArray


def mergeSort(array):
    """
    Sort function using merge sort algorithm.
    array - unsorted array
    """

    if len(array) > 1:
        mid = len(array) // 2

        # Sort left and right halves
        leftArray = mergeSort(array[:mid])
        rightArray = mergeSort(array[mid:])
        return merge(leftArray, rightArray)
    else:
        return array


def main():
    array = [10, 7, 8, 9, 1, 5, 34, 222, 1232, 6]

    print(mergeSort(array))


if __name__ == "__main__":
    main()
