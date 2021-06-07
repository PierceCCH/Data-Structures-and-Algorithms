class Node:
    def __init__(self, data):
        self.data = data
        self.front = None
        self.back = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    
    def peek(self):
        if self.last:
            return print("The last item is {}.".format(self.last.data))
        else:
            return print("The queue is empty bro")
    
    def enqueue(self, data):
        new_node = Node(data)
        if not self.first:
            self.first = new_node
            self.last = new_node
            self.length += 1
            return print("{} joined the queue".format(new_node.data))
        else:
            new_node.front = self.last
            self.last.back = new_node 
            self.last = new_node
            self.length += 1
            return print("{} joined the queue. {} is in front of it.".format(new_node.data, new_node.front.data))
    
    def dequeue(self):
        dequeued = self.first
        if not self.first:
            return print("Eh the queue is empty bro.")
        elif self.length == 1:
            self.first = None
            self.last = None
            self.length = 0
            return print("{} has left the queue.".format(dequeued.data))
        else:
            self.first = self.first.back
            self.first.front = None
            self.length -= 1
            return print("{} has left the queue.".format(dequeued.data))
    
    def showQueue(self):
        pt = self.first
        while pt != None:
            print("{} is in queue.".format(pt.data))
            pt = pt.back

q = Queue()
q.enqueue(5)
q.enqueue(8)
q.peek()
q.enqueue(3)
q.peek()
q.enqueue(54)
print()
q.showQueue()
print("Start leaving bois")
q.dequeue()
q.dequeue()
q.dequeue()
q.peek()
q.dequeue()




