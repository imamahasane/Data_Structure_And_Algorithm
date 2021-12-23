number = [3, 6, 2, 4, 3, 6, 8, 9]
dup = None

for i in range(len(number)):
    for j in range(i+1, len(number)):
        if number[i] == number[j]:
            dup = number[i]
            break
# Time Complexity: o(n^2)


for k in range(len(number)):
    if number[i] == number[j]:
        print(i)

# Time Complexity: o(n)

# time = a*n^2 + b*n + c 
#      = O(n^2)
