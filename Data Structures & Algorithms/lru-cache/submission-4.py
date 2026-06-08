class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next, self.prev = None, None
        

class LRUCache:

    def __init__(self, capacity: int):
        # hashmap to track key to node
        # doubly linked list head is pre MRU and tail is post LRU
        self.capacity = capacity
        self.hashmap = {}
        self.head = Node(0, 0)
        self.tail = Node (0, 0)
        self.head.next = self.tail 
        self.tail.prev = self.head

    def removeNode(self, node):
        # if next and prev, move around it
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev


    def updateMRU(self, key):
        # if node has prev and next, remove it from list
        node = self.hashmap[key]
        if node.prev and node.next:
            self.removeNode(node)

        # insert node in MRU spot
        # update MRU prev
        # update head next
        mru = self.head.next
        mru.prev = node

        node.prev = self.head
        node.next = mru

        self.head.next = node
        

    def get(self, key: int) -> int:
        # if not in hashmap returun -1
        if key not in self.hashmap:
            return -1

        # else update to MRU node
        self.updateMRU(key)
        return self.hashmap[key].val


    def put(self, key: int, value: int) -> None:
        # if capped, remove LRU
        if key not in self.hashmap and self.capacity == len(self.hashmap):
            lru = self.tail.prev
            self.removeNode(lru)
            del self.hashmap[lru.key]


        # if exists, update val and MRU
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
        else:
            self.hashmap[key] = Node(key, value)

        # else create new node and insert MRU
        self.updateMRU(key)

        
