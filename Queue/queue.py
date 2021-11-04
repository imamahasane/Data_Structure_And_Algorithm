class Queue:
    def __init__(self):
        self.items = []


    def enqueue(self, item):
        self.items.append(item)


    def dequeue(self):
        return self.items.pop(0)


    def is_empty(self):
        if self.items == []:
            return True
        return False


if __name__ == "__main__":
    q = Queue()
    q.enqueue("Imam")
    q.enqueue("Naima")
    q.enqueue("Samiul")

    while not q.is_empty():
        person = q.dequeue()
        print(person)
