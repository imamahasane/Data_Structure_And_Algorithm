
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, items):
         self.stack.append(items)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        if self.stack == []:
            return True
        return False     


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)

    while not s.is_empty():
        item = s.pop()
        print(item)

