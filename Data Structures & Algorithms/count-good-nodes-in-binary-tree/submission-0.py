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
        result = [0]
        
        def dfs(root, maxSeen):
            if not root:
                return 
            
            if root.val >= maxSeen:
                result[0] += 1
                maxSeen = max(maxSeen, root.val)
            
            dfs(root.left, maxSeen)
            dfs(root.right, maxSeen)
        
        dfs(root, root.val)
        return result[0]
