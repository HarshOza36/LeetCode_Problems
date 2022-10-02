class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # value are pointed to nodes, and key are the put values
        
        
        # left pointer = LRU
        # right pointer = Most Recently Used
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        
        
    # will remove the node in between left and right
    # say we had l-1-2-3-r, and delete 1
    # we will have l-2-3-r
    # we will just point prev.next to next and next.prev to prev of that
    # middle node
    def removeNode(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # inserting node such that, it becomes most recently used
    def insertNode(self, node):
        prev = self.right.prev
        nxt = self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
    
    def get(self, key: int) -> int:
        if key in self.cache:
            # if we get a node, we will have to make it most recently used
            self.removeNode(self.cache[key])
            self.insertNode(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeNode(self.cache[key])
        new = Node(key, value)    
        self.cache[key] = new
        self.insertNode(self.cache[key])
        
        # LRU logic
        if len(self.cache) > self.capacity:
            # remove LRU key
            lru = self.left.next
            self.removeNode(lru)
            self.cache.pop(lru.key)
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
