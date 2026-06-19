# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, total):
            if not node:
                return False
            if node.val + total == targetSum and not node.right and not node.left:
                return True
            
            if not node:
                return False
            
            if dfs(node.left, total + node.val):
                return True
            
            if dfs(node.right, total + node.val):
                return True
            return False
            
        return dfs(root, 0)
            