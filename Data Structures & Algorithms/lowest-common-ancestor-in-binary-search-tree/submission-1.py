# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # track all ancestors
        p_path = {}
        q_path = {}

        def dfs(root, target, depth, tracker):
            # base case
            if not root:
                return False
            
            # if found, or in subtrees track and return
            left = dfs(root.left, target, depth + 1, tracker)
            right = dfs(root.right, target, depth + 1, tracker)
            if root.val == target.val or left or right:
                tracker[root] = depth
                return True

            return False

        # populate all ancestors
        dfs(root, p, 0, p_path)
        dfs(root, q, 0, q_path)

        # find lowest
        result = [-float("inf"), None]

        for key in p_path.keys() & q_path.keys():
            depth = p_path[key]
            if depth > result[0]:
                result = [depth, key]

        return result[1]