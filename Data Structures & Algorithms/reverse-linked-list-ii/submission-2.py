# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        dummy = ListNode()
        dummy.next = head
        leftPrev = dummy

        curr = head
        # set curr to left
        for i in range(left - 1):
            leftPrev = curr
            curr = curr.next

        prev = None
        # reverse from left to right 
        for i in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # left prev is connected to new tail
        leftPrev.next.next = curr
        leftPrev.next = prev
        return dummy.next

