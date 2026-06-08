# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        preorder_i = 0
        index_dict = {} # preorder vals : in order index

        for i in range(len(inorder)):
            index_dict[inorder[i]] = i
        


        def dfs(left, right):
            nonlocal preorder_i

            if left > right:
                return
            
            node_val = preorder[preorder_i]
            node_index = index_dict[node_val]
            preorder_i += 1
            node = TreeNode(node_val)

            node.left = dfs(left, node_index - 1)
            node.right = dfs(node_index + 1, right)
            return node

            
        return dfs(0, len(inorder) - 1)