l = [1, 11, 9, 4, 2, 5, 7, 3, 6, 8, 10]
x = int(input("input hear(integer only): "))

for i in range(len(l)):
    if l[i] == x:
        print(f'your search number {x} was fount {i} index.')
        break
else:
    print("Sorry! Not found.")
