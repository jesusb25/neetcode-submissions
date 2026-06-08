# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # [1,2,3,4,5,6,7,8,9]
        def reverseLinkedList(head):
            # return head of reverse linked list
            prev = None
            curr = head
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev
        
        # init new head
        result = ListNode()

        # four ptrs left side, right side and middle list tail and head
        left = result
        result.next = head
        prev_tail = result
        right = head

        # f  1,2,3,4,5
        # lp r

        while True:
            for i in range(k):
                # break early if run off
                prev_tail = right
                if not right:
                    break
                # traverse so prev_tail becomes new head
                right = right.next
                
            # if no list to reverse
            if not prev_tail:
                break
            
            
            # break off and reverse middle list
            old_head = left.next
            prev_tail.next = None
            left.next = None
            new_head = reverseLinkedList(old_head)

            # attach middle list back
            left.next = new_head
            old_head.next = right

            # update left, right
            left = old_head
            

        return result.next
            


        



        