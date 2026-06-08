# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # go left and right tracking depth
        # return left depth + right 
        local = {}

        def populateLocals(root):
            if not root:
                return 0
            leftH, rightH = populateLocals(root.left), populateLocals(root.right)
            local[root] = leftH + rightH
            return 1 + max(leftH, rightH)
        populateLocals(root)

        return max(local.values())
            
