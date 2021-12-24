
def linear_s(book_list, user_input): 
    for i in range(len(book_list)):
        if book_list[i] == user_input:
            print(f'your search number {x} was fount {i} index.')
            break
    else:
        print("Sorry! Not found.")

l = [1, 11, 9, 4, 2, 5, 7, 3, 6, 8, 10]
x = int(input("input hear'integer only': "))
res = linear_s(l, x)
