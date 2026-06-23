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
        if not grid:
            return None
        
        val = grid[0][0]
        leaf = True
        root = Node(val)

        for row in grid:
            for num in row:
                if num != val:
                    leaf = False
            if not leaf:
                break
        
        root.isLeaf = leaf
        if leaf:
            return root
        
        mid = len(grid) // 2
        top_left = [row[:mid] for row in grid[:mid]]
        top_right = [row[mid:] for row in grid[:mid]]
        bot_right = [row[mid:] for row in grid[mid:]]
        bot_left = [row[:mid] for row in grid[mid:]]

        root.topLeft = self.construct(top_left)
        root.topRight = self.construct(top_right)
        root.bottomRight = self.construct(bot_right)
        root.bottomLeft = self.construct(bot_left)

        return root
    



        