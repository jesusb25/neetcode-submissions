"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # leaf means all vals same in grid
        if not grid:
            return None
        
        # check if leaf
        root = Node(1)
        nums = set()
        n = len(grid)
        for i in range(n):
            for j in range(n):
                nums.add(grid[i][j])
        if len(nums) == 1:
            root.val = bool(nums.pop())
            root.isLeaf = True
            return root
    
        root.isLeaf = False
    
        mid = n // 2
        top_left = [row[:mid] for row in grid[:mid]]
        top_right = [row[mid:] for row in grid[:mid]]
        bot_left = [row[:mid] for row in grid[mid:]]
        bot_right = [row[mid:] for row in grid[mid:]]
        root.topLeft = self.construct(top_left)
        root.topRight = self.construct(top_right)
        root.bottomLeft = self.construct(bot_left)
        root.bottomRight = self.construct(bot_right)
        return root
