import hashlib

class HashTable():
    def __init__(self, size=128):
        self.size = size
        self.data = [ [] for i in range(self.size)]

    def hash_key_to_index(self, key):
        return int(hashlib.md5( key.encode() ).hexdigest(), 16) % self.size
    
    def print_table(self):
        for item in self.data:
            print(item)

    def insert(self, key, value):
        hash_index = self.hash_key_to_index(key)
        self.data[hash_index].append({key: value})

    def search(self, key):
        hash_index = self.hash_key_to_index(key)
        for item in self.data[hash_index]:
            if key in item:
                return item
        return None
    
    def remove(self, key):
        hash_index = self.hash_key_to_index(key)
        for index,item in self.data[hash_index].enumerate:
            if key in item:
                del self.data[hash_index][index]
        return None