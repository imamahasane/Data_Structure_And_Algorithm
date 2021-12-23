number = [3, 6, 2, 4, 3, 6, 8, 9]

for i in range(len(number)):
    for j in range(i+1, len(number)):
        if number[i] == number[j]:
            print(f"{number[i]} is a duplicat")
            break
# Time Complexity: o(n^2)