my_list = [1, 3, 5, 9, 12, 45, 95, 120]
search = int(input())

for i in range(0, len(my_list)+1):
    if my_list[i] == search:
        print("pwa geche ", i)
        break
        
else:
    print("ei list er moddhe nai")