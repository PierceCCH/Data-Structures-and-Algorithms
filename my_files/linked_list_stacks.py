class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.bottom = None
        self.top = None
        self.height = 0
    
    def push(self, value):
        new_node = Node(value)

        if not self.top:
            self.bottom = new_node
            self.top = new_node
            self.height += 1
        else:
            new_node.next = self.top
            self.top = new_node
            self.height += 1
    
    def peek(self):
        return print("You peeked: {}".format(self.top.data)) if self.top else print("You got nothing bro")
    
    def pop(self):
        if not self.top:
            print("You got nothing bro")
        else:
            popped = self.top
            self.top = self.top.next
            self.height -= 1
        return popped.data

    def print_stack(self):
        i = 0
        temp = self.top
        if self.height == 0:
            print("No stack")
        while i<self.height:
            print("Number: {} | from top: {}".format(temp.data, i))
            i += 1
            temp = temp.next

s = Stack()
s.push(1)
s.push(1)
poo = s.pop()
print(poo)
s.print_stack()
