def find_price(price, eps, index):
    a =  price[index] / eps[index]
    return a

p = [11,22,33,44,55]
e = [1,2,3,4,5]

print(find_price(p, e, 2))

# Time Complexity: o(1)