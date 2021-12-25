class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)
    
    def size(self):
        return len(self.queue)

    def display(self):
        if len(self.queue) == 0:
            print("Sorry! empty")
        else:
            print(self.queue)

        a = self.size()
        print(a)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

q.dequeue()

q.display()
