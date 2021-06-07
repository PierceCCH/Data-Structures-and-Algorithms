class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
    
    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            raise "CANNOT PREPEND TO AN EMPTY LINKED LIST"
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def insert(self, index, data):
        new_node = Node(data)
        i = 0
        temp = self.head
        if index >= self.length:
            self.append(data)
            return
        elif index == 0:
            self.prepend(data)
            return
        else:
            while i<self.length:
                if i == index - 1:
                    temp.next, new_node.next = new_node, temp.next
                    self.length += 1
                    return
                temp = temp.next
                i += 1
    
    def remove(self, index):
        i = 0
        temp = self.head
        if index>=self.length:
            print("Entered wrong index")
        
        if index == 0:
            self.head = self.head.next
            self.length -= 1   
            return

        while i<self.length:
            if i == index - 1:
                temp.next = temp.next.next
                self.length -= 1
                return
            temp == temp.next
            i += 1
    
    def reverse(self):
        prev = None
        curr = self.head
        next = None
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev


    def printl(self):
        temp = self.head
        while temp != None:
            print(temp.data , end = ' ')
            temp = temp.next
            print()
            print('Length = '+str(self.length))
            

    
ll = LinkedList()
ll.append(5)
ll.append(6)
ll.append(7)
ll.insert(0, 2)
ll.insert(8, 2)
ll.insert(3, 2)
ll.printl()
print("\nREVERSAL TIME")
ll.reverse()
ll.printl()


