def insertion_sort(valu):
    n = len(valu)

    for i in range(1, n):
        items = valu[i]
        j = i - 1

        while j >= 0 and valu[j] > items:
            valu[j+1] = valu[j]
            j -= 1
            valu[j+1] = items


if __name__ == "__main__":
    l = [1, 11, 9, 7, 6, 10, 4, 5, 2, 3,  8]
    print(f"befor insertion sort: {l}")

    insertion_sort(l)
    print(f"after insertion sort: {l}")