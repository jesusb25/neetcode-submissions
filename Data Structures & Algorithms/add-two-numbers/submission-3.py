# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # easy pull both numbers, sum then extend into linked list
        # optimized iterate once carrying over nums
        carry = 0
        result = ListNode()
        curr = result
        while l1 or l2 or carry:
            # calc sum
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            total = l1_val + l2_val + carry
            
            # new digit
            carry = total // 10
            total = total % 10
            
            new_node = ListNode(total)

            # traverse
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr.next = new_node
            curr = new_node
        return result.next

