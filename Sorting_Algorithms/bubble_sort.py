def bubbleSort(L):
    n = len(L)

    for i in range(0, n):
        for j in range(0, n-i-1):
            if L[j] > L[j+1]:
                L[j], L[j + 1] = L[j + 1], L[j]


if __name__ == "__main__":
    aa = [9, 2, 1, 6, 4, 8, 3, 5, 7]
    print(f"Before sort: {aa}")
    
    bubbleSort(aa)
    print(f"After sort: {aa}")