# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # dfs pre order traversal checking all left keys are smaller and all right keys are bigger
        # flatten tree check orders
        # in order traversal

        result = []

        def dfs(node):
            if not node:
                return 
            
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        dfs(root)
        for i, num in enumerate(result):
            if i == 0:
                continue
            if num <= result[i - 1]:
                return False
        return True

        


        