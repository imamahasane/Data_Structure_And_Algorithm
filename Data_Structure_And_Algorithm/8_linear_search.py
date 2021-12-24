
def linear_search(book_list, user_input): 
    for i in range(len(book_list)):
        if book_list[i] == user_input:
            return i
    return -1

l = [1, 11, 9, 4, 2, 5, 7, 3, 6, 8, 10]
x = int(input("input hear'integer only': "))
res = linear_search(l, x)

if res == -1:
    print("Sorry! Not found.")

else:
    print(f'your search number {x} was fount')


