def BinarySearch(L, x):
    left, right = 0, len(L) - 1

    while left <= right:
        mid = (left + right) // 2

        if L[mid] == x:
            return mid
        
        elif L[mid] < x:
            left = mid + 1

        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 100]

    for x in range(1, 11):
        position = BinarySearch(L, x)

        if position == -1:
            if x in L:
                print(x, "is in L, but function returened -1")

            else:
                print(x, "is not List")

        else:
            if L[position] == x:
                print(x, "Found the correct position.")

            else:
                print("binary search returend", position, "for", x, "which is incorrect")

    print("Program Terminated")