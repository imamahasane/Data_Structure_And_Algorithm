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
            node.prev = self.head
            self.tail = node
            self.size += 1

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
            vals.append(node.val)
            node = node.next
        return f"[{', '.join(str(val) for val in vals)}]"


myList = DoubleLinkList()
myList.add(1)
myList.add(5)
myList.add(2)
myList.add(21)

print(myList)
print(myList.size)


        
