class HashTable:

    def __init__(self,size):
        self.size = size
        self.keys = size * [None] 
        self.values = size * [None] 

    def hashfuntion(self,key):
        return hash(key) % self.size

    def insert(self,key,value):
        index = self.hashfuntion(key)
        while self.keys[index]  is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return "The value is inserted"
            index = (index + 1) % self.size
        self.keys[index] = key
        self.values[index] = value
    def search(self,key):
        try:
            index = self.hashfuntion(key)
            while self.keys[index] is not None:
                if self.keys[index] == key:
                    return self.values[index]
                index = (index + 1) % self.size
            raise Exception("Key is not found")
        except Exception as keyerr:
            return str(keyerr)

        finally:
            "Search is completed"

    def delete(self,key):
        index = self.hashfuntion(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = None
            


ht = HashTable(6)


ht.insert('q',40)
ht.insert('E',50)
ht.insert('J',440)
ht.insert('Y',440)

print(ht.search('J'))


class HashTable:
    def __init__(self,size):
        self.size = size 
        self.values = None * size
        self.keys = None * size