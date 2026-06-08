# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs level order traversal
        # reverse every other parts
        if not root: return []
        result = []
        q = deque()
        q.append([root])
        
        while q:
            nodes = q.popleft()
            if nodes == []: break
            
            level = []
            next_nodes = []
            for node in nodes:
                level.append(node.val)

                if node.left:
                    next_nodes.append(node.left)
                
                if node.right:
                    next_nodes.append(node.right)

            q.append(next_nodes)
            if len(result) % 2 != 0:
                result.append(level[::-1])
            else:
                result.append(level)
        return result

        