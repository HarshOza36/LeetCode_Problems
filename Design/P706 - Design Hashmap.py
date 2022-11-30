class Buckets:
    def __init__(self,):
        self.bucket = []

    def get(self, key):
        for k, v in self.bucket:
            if k == key:
                return v
        return -1
    
    def update(self, key, value):
        for idx, (k, v) in enumerate(self.bucket):
            if k == key:
                # if key exists update
                self.bucket[idx] = (key, value)
                break
        else:
            # else append it to bucket
            self.bucket.append((key, value))

    def remove(self, key):
        for idx, (k, v) in enumerate(self.bucket):
            if k == key:
                print(self.bucket[idx])
                del self.bucket[idx]
            
class MyHashMap(object):
    def __init__(self):
        self.modulus = 2069 # to avoid collisions prime number modulus
        self.hash_map = [Buckets() for i in range(self.modulus)]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        hash_key = key % self.modulus
        self.hash_map[hash_key].update(key, value)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        hash_key = key % self.modulus
        return self.hash_map[hash_key].get(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash_key = key % self.modulus
        self.hash_map[hash_key].remove(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)