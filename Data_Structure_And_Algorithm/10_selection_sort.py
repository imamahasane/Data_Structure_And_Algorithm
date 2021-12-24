def selection_sort(valu):
    n = len(valu)

    for i in range(n-1):
        min_index = i

        for j in range(i+1, n):
            if valu[min_index] > valu[j]:
                min_index = j

        valu[min_index], valu[i] = valu[i], valu[min_index]        

if __name__ == "__main__":
    l = [1, 11, 9, 4, 2, 5, 7, 3, 6, 8, 10]
    print(f"befor selection sort: {l}")

    selection_sort(l)
    print(f"after selection sort{l}")
