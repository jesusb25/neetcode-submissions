# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # go left right return 0 at null
        # return 1 + max recurse left and recurse righ
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        