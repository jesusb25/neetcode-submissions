# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        res = head
        head1 = head
        head2 = prev

        while head1 and head2:
            next_head1 = head1.next
            head1.next = head2
            head1 = next_head1

            next_head2 = head2.next
            head2.next = next_head1
            head2 = next_head2
        



