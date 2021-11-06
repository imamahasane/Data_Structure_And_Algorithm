def selectionSort(L):
    n = len(L)

    for i in range(0, n - 1):
        index_min = i

        for j in range(i + 1, n):
            if L[j] < L[index_min]:
                index_min = j

        if index_min != i:
            L[i], L[index_min] = L[index_min], L[i]


if __name__ == "__main__":
    aa = [9, 2, 1, 6, 4, 8, 3, 5, 7]
    print(f"Before sort: {aa}")
    
    selectionSort(aa)
    print(f"After sort: {aa}")