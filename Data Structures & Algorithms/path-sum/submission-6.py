# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(curr, rem):
            if not curr:
                return False
            
            if rem - curr.val == 0 and not curr.left and not curr.right:
                return True
            
            if dfs(curr.left, rem - curr.val):
                return True
            
            if dfs(curr.right, rem - curr.val):
                return True
            
            return False

        return dfs(root, targetSum)