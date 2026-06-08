# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        local = set()
        # store locals
        # node val : local max paths
        # local diameter

        def dfs(root):
            if not root:
                return 0
                
            
            # path through left
            left = dfs(root.left)

            # path through right
            right = dfs(root.right)

            # path through both and store
            local.add(root.val + max(0, left, right, left + right))
            return root.val + max(0, left, right)

        root_path = dfs(root)
        return max([dfs(root)] + list(local))