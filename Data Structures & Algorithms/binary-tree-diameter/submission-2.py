# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = [0]

        def findDiameters(root):
            if not root:
                return 0
            
            leftD = findDiameters(root.left) if root.left else 0
            rightD = findDiameters(root.right) if root.right else 0

            result[0] = max(result[0], leftD + rightD)
            return 1 + max(leftD, rightD)
        
        findDiameters(root)
        return result[0]