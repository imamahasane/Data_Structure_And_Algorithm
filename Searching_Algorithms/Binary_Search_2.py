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

    position = BinarySearch(L, 100)
    print(position)