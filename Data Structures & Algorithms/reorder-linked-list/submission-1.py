# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # reverse second half of linked list then merge
        # [0, 1, 2, 3, 4, 5, 6]
        # [0, 6, 1, 5, 4, 3]


        # [0, 1, 2, 3]
        
        # [0, 3, 1, 2]
        # count length
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        # get to length
        curr = head
        prev = None
        for i in range(math.ceil(count / 2)):
            prev = curr
            curr = curr.next
        prev.next = None
        # reverse linked list
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        second_head = prev

        # combine linked lists
        first_head = head
        while first_head and second_head:
            nxt1 = first_head.next
            nxt2 = second_head.next
            first_head.next = second_head
            second_head.next = nxt1

            first_head = nxt1
            second_head = nxt2

        