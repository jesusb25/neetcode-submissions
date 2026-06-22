# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = []

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            arr.append(node)
            dfs(node.right)
        dfs(root)
        
        node1 = None
        node2 = None
    
        for i in range(len(arr) - 1):
            if arr[i].val > arr[i + 1].val:
                node2 = arr[i + 1]
                if not node1:
                    node1 = arr[i]
                else:
                    break
        
                
        
        node1.val, node2.val = node2.val, node1.val
        

