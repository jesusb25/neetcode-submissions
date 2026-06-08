# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = ListNode()
        curr = result

        while True:
            min_index = -1

            for i, node in enumerate(lists):
                if not node:
                    continue

                if min_index == -1 or node.val < lists[min_index].val:
                    min_index = i
                
            if min_index == -1:
                break
            
            curr.next = lists[min_index]
            curr = curr.next
            lists[min_index] = lists[min_index].next

        return result.next




