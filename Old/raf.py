
def binarySearch(my_list, left, right, search):
    while left <= right:
        mid = int((left + right) / 2)
        
        if my_list[mid] == search:
            return mid
        
        elif my_list[mid] < search:
            left = mid + 1
            
        else:
            right = mid - 1
    
my_list = [1, 3, 5, 9, 12, 45, 95, 120]
search = int(input())


result = binarySearch(my_list, 0, len(my_list) - 1, search)

if result != -1:
    print("List er vitor asa ")    
else:
    print("List er vitor nai vaia")