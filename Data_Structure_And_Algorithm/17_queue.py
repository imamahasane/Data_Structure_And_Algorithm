
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        return self.items.append(value)

    def dequeue(self):
        if self.items == []:
            return None
        else:
            self.items.pop(0)

    def desplay(self):
        if len(self.items) == 0:
            print("Sorry! empty")
        else:
            print(self.items)


if __name__ == "__main__":
    value = Queue()

    value.enqueue("imam")
    value.enqueue("anan")
    value.enqueue("manan")
    value.enqueue("iiiiii")
    value.dequeue()
    

    value.desplay()
