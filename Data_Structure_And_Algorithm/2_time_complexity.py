def get_squared(number):
    square_number = []

    for i in number:
        square_number.append(i * i)

    return square_number

n = [2, 5, 8, 9]
re = get_squared(n)
print(re)

# Time Complexity: o(n)
