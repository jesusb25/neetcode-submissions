# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        while curr:
            if curr == q or curr == p:
                return curr
            
            if curr.val > max(p.val, q.val):
                curr = curr.left
            elif curr.val < min(p.val, q.val):
                curr = curr.right
            else:
                return curr
        return None