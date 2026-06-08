# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # return true if both null
        if not p and not q:
            return True
        
        # return false if one doesnt exist
        if not p or not q:
            return False
        
        # return false if  val p != val q 
        if p.val != q.val:
            return False
        
        # return subtrees are equal
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)