class Queue():
    def __init__(self):
        self.data = []
    
    def enqueue(self, element):
        return self.data.append(element)

    def dequeue(self):
        return self.data.pop(0)