# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def dfs(root, maxSeen):
            res = 0
            if not root:
                return 0
            
            if root.val >= maxSeen:
                res += 1
                maxSeen = max(maxSeen, root.val)
            
            return res + dfs(root.left, maxSeen) + dfs(root.right, maxSeen)
        
        return dfs(root, root.val)
        
