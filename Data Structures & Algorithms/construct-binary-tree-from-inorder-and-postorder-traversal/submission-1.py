# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        indexMap = {num : i for i, num in enumerate(inorder)}

        def dfs(l, r):
            if l > r:
                return None
            
            root = TreeNode(postorder.pop())
            index = indexMap[root.val]
            root.right = dfs(index + 1, r)
            root.left = dfs(l, index - 1)
            return root
        return dfs(0, len(inorder) - 1)