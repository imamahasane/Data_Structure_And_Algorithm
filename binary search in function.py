def binarySearch(my_list, search):
    left = 0
    right = len(my_list) - 1
    
    while left <= right:
        mid = int((left + right) / 2)
        
        if my_list[mid] == search:
            return mid
        
        elif my_list[mid] < search:
            left = mid + 1
        
        else:
            right = mid - 1
    return -1

my_list = [1, 3, 5, 9, 12, 45, 95, 120]
search = int(input())
result = binarySearch(my_list, search)

if result != -1:
    print("pwa geche", result)
    
else:
    print("pwa jai nai re vaia!!!!!!")