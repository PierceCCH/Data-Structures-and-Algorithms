class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
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
            return
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1
            return
    
    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            raise "CANNOT PREPEND TO AN EMPTY LINKED LIST"
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return

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
                    new_node.next = temp.next
                    temp.next.prev = new_node
                    temp.next = new_node
                    new_node.prev = temp
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

    def printl(self):
        temp = self.head
        while temp != None:
            print(temp.data , "| current: ", temp, "prev: ", temp.prev, end = ' |')
            temp = temp.next
            print()
            print('Length = '+str(self.length))

ls = DoublyLinkedList()
ls.append(5)
ls.append(6)
ls.append(7)
ls.insert(1,4)
ls.printl()