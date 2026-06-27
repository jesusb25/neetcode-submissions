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

            if total + curr.val == targetSum and not curr.left and not curr.right:
                return True
                
            
            return dfs(curr.right, total + curr.val) or dfs(curr.left, total + curr.val)

        return dfs(root, 0)