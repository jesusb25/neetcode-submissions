class Node:
    def __init__(self, val = 0, prev = None, next = None, key = None):
        self.val = val
        self.prev = prev
        self.next = next
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.hashmap = {} # key to node

    def removeNode(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev
    
    def insertNode(self, node):
        tmp = self.head.next
        self.head.next = node
        node.prev = self.head
        tmp.prev = node
        node.next = tmp

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        self.put(key, self.hashmap[key].val)
        return self.hashmap[key].val
        
    def put(self, key: int, value: int) -> None:
        # insert or update
        if key not in self.hashmap:
            # create node
            node = Node()
            node.key = key
            self.hashmap[key] = node
        else:
            # remove from list
            node = self.hashmap[key]
            self.removeNode(node)

        node.val = value
        self.insertNode(node)

        # remove lru if full
        if len(self.hashmap) > self.capacity:
            lru = self.tail.prev
            self.removeNode(lru)
            del self.hashmap[lru.key]





        
            

