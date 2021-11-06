def binary_search_recursive(L, left, right, x):
    if left > right:
        return -1

    mid = (left + right) // 2
    if L[mid] == x:
        return mid

    if L[mid] < x:
        return binary_search_recursive(L, mid + 1, right, x)

    else:
        return binary_search_recursive(L, left, mid - 1, x)


if __name__ == "__main__":
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
    left = 0
    right = len(L) - 1

    for x in range(1, 11):
        position = binary_search_recursive(L, left, right, x)

        if position == -1:
            if x in L:
                print(x, "is in L, but function retured - 1")

            else:
                print(x, "not is list")

        else:
            if L[position] == x:
                print(x, "Found the correct position.")

            else:
                print("binary search returend", position, "for", x, "which is incorrect")

    print("Program Terminated")