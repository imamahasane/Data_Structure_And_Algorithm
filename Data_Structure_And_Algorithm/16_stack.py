
def is_balanced(input_str):
    s = list()

    for ch in input_str:
        if ch == '(':
            s.append(ch)

        if ch == ')':
            if not s:
                return False
            s.pop()
    return not s

if __name__ == "__main__":
    input_str = input("Please input hear: ")

    if is_balanced(input_str):
        print(f"{input_str} is balanced.")
    else:
        print(f"{input_str} is not balanced.")
            