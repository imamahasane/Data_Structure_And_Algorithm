arr = [1, 5, 7, 11, 15, 30, 35, 40, 50]
left = 0
search = 50
mid = 0
right = len(arr)-1

print(right)

while left <= right:
    mid = int((left + right) / 2)      
 
    if arr[mid] == search:
        print(arr[mid])
        break
    
    elif arr[mid] < search:
        left = mid + 1
        
    else:
        right = mid - 1