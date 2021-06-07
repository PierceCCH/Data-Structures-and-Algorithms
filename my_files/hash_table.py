class HashTable:
    def __init__(self):
        self.bucket = 16
        self.data = [[] for i in range(self.bucket)]
    
    def __str__(self):
	    return str(self.__dict__)
    
    def hash_value(self, key):
        return len(key)%self.bucket
    
    def put(self, key, value):
        hash = self.hash_value(key)
        bucket = self.data[hash]

        #done to deal with collisions
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i][i] = value
                return None
        bucket.append([key, value])
    
    def get(self, key):
        bucket = self.data[self.hash_value(key)]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                return bucket[i][1]
        return -1
    
    def remove(self, key):
        bucket = self.data[self.hash_value(key)]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                return -1
    
    def keys(self):
        keys_array = []
        for bucket in self.data:
            if bucket: #O(n^2) time hmmm
                for i in range(len(bucket)):
                    keys_array.append(bucket[i][0])
        return keys_array


ht = HashTable()
ht.put("Jonny", "coder")
ht.put("Samy", "loner")
ht.put("Lanny", "wanker")
print(ht.keys())
print(ht.get("Lanny"))
ht.remove("Jonny")
print(ht)
    