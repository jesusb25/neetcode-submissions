# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        seen = set()
        res = []

        def dfs(node, h):
            if not node:
                return
            
            if h not in seen:
                res.append(node.val)
            seen.add(h)
            
            dfs(node.right, h + 1)
            dfs(node.left, h + 1)
        dfs(root, 0)
        return res