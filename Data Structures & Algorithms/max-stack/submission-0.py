class ListNode:

    def __init__(self, val = 0, prev = None, next = None):
        self.next = next
        self.val = val
        self.prev = prev
        self.deleted = False

class MaxStack:
    def __init__(self):
        # linked list reps stack
        self.heap = [] # max heap [[-val, -order_inserted, node]]
        self.head = ListNode()
        self.tail = ListNode(0, self.head)
        self.head.next = self.tail
        self.nodes = 0
        self.deleted = set()

    def push(self, x: int) -> None:
        # insert to heap, insert next to tail
        left_node = self.tail.prev
        right_node = self.tail
        new_node = ListNode(x, left_node, right_node)
        left_node.next = new_node
        self.tail.prev = new_node
        heapq.heappush(self.heap, [-x, -self.nodes, new_node])
        self.nodes += 1

    def pop(self) -> int:
        pop_node = self.tail.prev
        left_node = pop_node.prev
        left_node.next = self.tail
        self.tail.prev = left_node
        self.deleted.add(pop_node)
        return pop_node.val

    def top(self) -> int:
        top = self.tail.prev
        return top.val



    def peekMax(self) -> int:
        while self.heap and self.heap[0][2] in self.deleted:
            heapq.heappop(self.heap)
            
        return -self.heap[0][0]
        

    def popMax(self) -> int:
        while self.heap and self.heap[0][2] in self.deleted:
            heapq.heappop(self.heap)
        
        max_node = self.heap[0][2]
        left_node, right_node = max_node.prev, max_node.next
        self.deleted.add(max_node)
        left_node.next = right_node
        right_node.prev = left_node
        heapq.heappop(self.heap)

        return max_node.val


        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
