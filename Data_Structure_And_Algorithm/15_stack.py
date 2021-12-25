
stack = []
def push(valu):
    stack.append(valu)


def pop():
    if len(stack) == 0:
        print("Sorry! stack empaty.")
    else:
        # a = stack.pop()
        return stack.pop()
    
        

push(1)
print(stack)

push(2)
print(stack)

push(22)
print(stack)

push(23)
print(stack)

push(14)
print(stack)

push(25)
print(stack)

pop()
print(stack)