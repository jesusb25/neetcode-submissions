# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        # get length of list
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # traverse to n of list
        dummy = ListNode()
        dummy.next = head

        prev = dummy
        curr = head
        for i in range(length - n):
            prev = curr
            curr = curr.next

        # remove nth node
        prev.next = curr.next

        return dummy.next
        