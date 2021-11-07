def merge(a, b):
    merged_list = []
    len_a, len_b = len(a), len(b)
    index_a, index_b = 0, 0

    while index_a < len_a and index_b < len_b:
        if a[index_a] < b[index_b]:
            merged_list.append(a[index_a])
            index_a += 1

        else:
            merged_list.append(b[index_b])
            index_b += 1
    return merged_list


if __name__ == "__main__":
    a = [1]
    b = [2]
 
    expectrd_merged_list = [1, 2]
    merged_list = merge(a, b)
    