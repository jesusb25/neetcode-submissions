# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        
        # 1. dfs right then left

        def dfs(root, level):
            if not root:
                return
            
            # 2. if first node at such depth then must be right most node
            if level > len(result):
                result.append(root.val)
            dfs(root.right, level + 1)
            dfs(root.left, level + 1)
        # 3. return result
        dfs(root, 1)
        return result
        