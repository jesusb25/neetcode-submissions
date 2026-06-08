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
        
        def dfs(node, maxSeen):
            res = 0
            if not node:
                return 0
            
            if node.val >= maxSeen:
                res += 1
                maxSeen = node.val
            return res + dfs(node.left, maxSeen) + dfs(node.right, maxSeen)
        
        return dfs(root, root.val)
        
