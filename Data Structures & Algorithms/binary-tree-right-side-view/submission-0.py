# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 1. bfs holding all values
        if not root:
            return []
        q = deque()
        q.append([root, 0])
        levels = []
        
        while q:
            node, index = q.popleft()
            if not node:
                continue

            if index + 1 > len(levels):
                levels.append([])
            levels[index].append(node.val)

            q.append([node.left, index + 1])
            q.append([node.right, index + 1])
        
        # 2. go through and collect right most values at each level
        result = []
        for level in levels:
            result.append(level[-1])
        # 3. return result
        return result
        