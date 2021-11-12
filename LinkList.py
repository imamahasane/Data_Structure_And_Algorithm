class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.val = value


class DoubleLinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, val):
        node = Node(val)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.size += 1

        else:
            self.head.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1

    def __remove_node(self, node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

        self.size -= 1

    def remove(self, value):
        node = self.head
        while node is not None:
            if node.val == value:
                self.__remove_node(node)
            node = node.next


    def __str__(self):
        vals = []
        node = self.head
        while node is not Node:
            vals.append(self.node)
            node = node.next
        return f"[{', '.join(str(val) for val in vals)}]"


myList = DoubleLinkList()
myList.add(1)
myList.add(5)
myList.add(2)
myList.add(21)
print(myList)

myList.remove(21)
print(myList)
myList.remove(1)
print(myList)

# print(myList.size)