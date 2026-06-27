# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(curr, total):
            if not curr:
                return False
            
            total += curr.val
            if not curr.left and not curr.right:

                return total == targetSum
            return dfs(curr.left, total) or dfs(curr.right, total)
        return dfs(root, 0)