# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        # traverse through postorder in reverse
        # current index in post order is root
        # left of root is left subtree
        # right of root is right substree
        index = [len(inorder) - 1]
        def dfs(left, right):
            if left > right:
                return None
            root_index = inorder.index(postorder[index[0]])
            root_node = TreeNode(postorder[index[0]])
            index[0] -= 1
            if left == right:
                return root_node
            
            root_node.right = dfs(root_index + 1, right)
            root_node.left = dfs(left, root_index - 1)
            return root_node



        
        return dfs(0, len(postorder) - 1)


        