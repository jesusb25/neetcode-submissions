class Node():
    
    def __init__(self, key = None, val = None, prev = None, next = None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        # head
        self.head = Node()

        # tail
        self.tail = Node()
        self.tail.prev = self.head
        self.head.next = self.tail

        # capacity
        self.c = capacity

        # kick out least recently used
        self.hashmap = {} # key to node


    def removeNode(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

    def insertNode(self, node):
        prev_next = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = prev_next
        prev_next.prev = node

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        node = self.hashmap[key]
        self.removeNode(node)
        self.insertNode(node)
        return node.val

        
    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.removeNode(node)
        else:
            self.c -= 1
            node = Node(key)
            self.hashmap[key] = node

        node.val = value
        self.insertNode(node)

        # remove node if needed
        if self.c == -1:
            lru = self.tail.prev
            self.removeNode(lru)
            del self.hashmap[lru.key]
            self.c += 1

    

            
        
        
