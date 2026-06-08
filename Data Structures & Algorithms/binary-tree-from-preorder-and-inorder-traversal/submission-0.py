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
        preorder_i =[0]
        index_dict = {}
        for i in range(len(inorder)):
            index_dict[inorder[i]] = i
        

        def divideAndConquer(left, right):
            if left > right:
                return None
            print(f"left: {left}, right: {right}")
            next_root = preorder[preorder_i[0]]
            preorder_i[0] += 1

            root_index = index_dict[next_root]
            root = TreeNode(next_root)
            if left == right:
                return root

            root.left = divideAndConquer(left, root_index - 1)
            root.right = divideAndConquer(root_index + 1, right)
            return root


        return divideAndConquer(0, len(inorder) - 1)



