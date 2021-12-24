
def binary_search(n, f):
    left = 0
    right = len(n)-1

    while left <= right:
        mid = (left + right) // 2
        if n[mid] == f:
            return mid
        if n[mid] < f:
            left = mid + 1
        else:
            right = mid  - 1
    return -1
        
numbers = [1,4,6,9,11,15,17,21,34,56]
number_to_find = int(input("Please your input hear: "))
re = binary_search(numbers, number_to_find)

if re != -1:
    print(f"Searching number {number_to_find} was found")
    
else:
    print("Not found.")

