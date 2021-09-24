arr = [1, 5, 7, 11, 15, 30, 35, 40, 50]
search = 400

for i in range(0, len(arr)):
    if arr[i] == search:
        print("asa vai:", i)
        break
else:
    print("Nai")