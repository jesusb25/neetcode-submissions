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
        copyMap = {None:None}

        curr = head
        while curr:
            if curr not in copyMap:
                copyMap[curr] = Node(curr.val)
            if curr.next not in copyMap:
                copyMap[curr.next] = Node(curr.next.val)
            if curr.random not in copyMap:
                copyMap[curr.random] = Node(curr.random.val)
            new = copyMap[curr]
            new.random = copyMap[curr.random]
            new.next = copyMap[curr.next]
            curr = curr.next
        return copyMap[head]

            
            
            