# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        vals = []

        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            vals.append(root.val)
            dfs(root.right)
        
        dfs(root)
        return vals[k - 1]


        