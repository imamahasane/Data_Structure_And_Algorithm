def bubble_sort(valu):
    n = len(valu)

    for i in range(n):
        for j in range(0, n-i-1):
            if valu[j] > valu[j+1]:
                valu[j], valu[j+1] = valu[j+1], valu[j]

if __name__ == "__main__":
    l = [1, 11, 9, 7, 6, 10, 4, 5, 2, 3,  8]
    print(f"befor bubble sort: {l}")

    bubble_sort(l)
    print(f"after bubble sort: {l}")
