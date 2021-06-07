class Array:
    def __init__(self):
        self.length = 0
        self.data = {}
    
    def __str__(self):
        return str(self.__dict__)
    
    def append(self, item):
        self.data[self.length] = item
        self.length+=1
    
    def pop(self):
        deletedItem = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return deletedItem
    
    def delete(self, index):
        deletedItem = self.data[index]
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length - 1]
        return deletedItem
    
    def lookUp(self, index):
        return self.data[index]

    def insert(self, item, index):
        for i in range(self.length, index, -1):
            self.data[i] = self.data[i-1]
        self.data[index] = item
        self.length+=1
    
    def flip(self):
        for i in range(int(self.length/2)):
            temp = self.data[i]
            self.data[i] = self.data[self.length - i - 2]
            self.data[self.length-i-2] = temp

arr = Array()
arr.append('Hi')
arr.append('there')
arr.append('retard')
arr.insert('X', 1)
arr.insert('X', 1)
arr.insert('yay', 3)
arr.delete(3)
print(arr)
print(arr.lookUp(1))
arr.flip()
print(arr)

