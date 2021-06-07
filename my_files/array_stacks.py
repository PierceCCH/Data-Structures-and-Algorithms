class Stack:
    def __init__(self):
        self.array = []
        self.height = len(self.array)
    
    def __str__(self):
        return str(self.__dict__)

    def push(self, data):
        self.array.append(data)
    
    def pop(self):
        popped = self.array[self.height-1]
        self.array.pop()
        return popped
    
    def peek(self):
        print("Peeked: {}".format(self.array[-1]))

arr =Stack()
arr.push(5)

