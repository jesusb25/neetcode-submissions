"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        # map old node to new node
        matches = {}

        # then create new node neighbors using mappings and previous
        def dfs(curr):
            matches[curr] = Node(curr.val)

            for neighbor in curr.neighbors:
                if neighbor not in matches:
                    dfs(neighbor)
            
        
        dfs(node)
        
        for old, new in matches.items():
            for neighbor in old.neighbors:
                new_neighbor = matches[neighbor]
                new.neighbors.append(new_neighbor)
        return matches[node]


        

