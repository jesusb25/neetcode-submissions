"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {None: None}

        curr = head
        while curr:
            new_node = Node(curr.val)
            old_to_new[curr] = new_node
            curr = curr.next
        
        for old_node, new_node in old_to_new.items():
            if old_node:
                new_node.next = old_to_new[old_node.next]
                new_node.random = old_to_new[old_node.random]
        
        return old_to_new[head]