def Linear_Search(L, x):
    n = len(L)
    i = 0
    while i < n:
        if L[i] == x:
            return i
        i += 1
    i = -1
    return i

if __name__ == "__main__":
    a = [1, 2, 3, 4,10, 100, 222, 55, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99]
    LS = Linear_Search(a, 5)
    print(LS)