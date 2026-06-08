# doubly linked list 
class Node:

    def __init__(self, key = None, val = 0, prev = None, nxt = None):
        self.val = val
        self.next = nxt
        self.prev = prev
        self.key = key

class LRUCache:



    def __init__(self, capacity: int):
        # capacity max
        self.hashmap = {} # key: node
        self.capacity = capacity
        self.most_recent = Node()
        self.lru = Node()
        # dummy <-> [key 1, key 2, key 3] <-> tail
        self.most_recent.next = self.lru
        self.lru.prev = self.most_recent
    
    def updateRecent(self, key):
        node = self.hashmap[key]
        prev, next = node.prev, node.next
        if prev and next:
            prev.next = next
            next.prev = prev
        node.next = self.most_recent.next
        self.most_recent.next = node
        node.prev = self.most_recent
        node.next.prev = node

    def get(self, key: int) -> int:
        # if key exists, return value otherwise -1
        if key in self.hashmap:
            self.updateRecent(key)
            return self.hashmap[key].val
        return -1
        
        

    def put(self, key: int, value: int) -> None:
        # if key exists, update value
        if key in self.hashmap:
            self.updateRecent(key)
            self.hashmap[key].val = value
            return
        
        # evict lru
        if self.capacity == 0:
            self.capacity += 1
            lru_node = self.lru.prev
            del self.hashmap[lru_node.key]
            prev = lru_node.prev
            prev.next = self.lru
            self.lru.prev = prev
            
        # add new node
        new = Node(key, value)
        self.hashmap[key] = new
        self.updateRecent(key)
        self.capacity -= 1
        

            







