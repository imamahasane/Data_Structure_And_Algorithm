def Linear_Search(L, x):
    n = len(L)

    for i in range(n):
        if L[i] == x:
            return i
    return -1


if __name__ == "__main__":
    a = [1, 2, 3, 4,10, 100, 222, 55, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99]
    LS = Linear_Search(a, 5)
    print(LS)