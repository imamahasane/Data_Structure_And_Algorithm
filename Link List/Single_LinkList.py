class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class LinkList:
    def __init__(self):
        self.head = Node()


    def __repr__(self):
        nodes = []
        current_node = self.head.next

        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.next
        return ",".join(nodes)


    def append(self, data):
        node = Node(data)
        if self.head.next is None:
            self.head.next = node
            return
        
        current_node = self.head.next

        while current_node.next:
            current_node = current_node.next
        current_node.next = node


    def prepend(self, data):
        node = Node(data, self.head.next)
        self.head.next = node


    def insert(self, data, new_data):
        current_nodde = self.head.next

        while current_nodde:
            if current_nodde.data == data:
                current_nodde.next = new_data
                break
            current_nodde = current_nodde.next


    def search(self, item):
        current_node = self.head.next

        while current_node:
            if current_node.data == item:
                return current_node
            current_node = current_node.next
            return None


    def remove(self, item):
        previous_node = self.head
        current_node = previous_node.next

        while current_node:
            if current_node.data == item:
                break

            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return None

        if self.head == previous_node:
            self.head.next = current_node.next

        else:
            previous_node.next = current_node.next

if __name__ == "__main__":
    ll = LinkList()

    ll.append(5)
    ll.append(51)
    ll.append(11)
    ll.append(61)
    print(ll)

    ll.prepend(1)
    print(ll)

    ll.remove(5)
    print(ll)
