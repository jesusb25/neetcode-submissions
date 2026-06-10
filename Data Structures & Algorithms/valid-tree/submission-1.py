class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # all nodes reachable, no cycles, and n-1 edges
        if len(edges) != n - 1:
            return False
        
        adj = defaultdict(list) # node: neighbors
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        # marked visited after all neighbors
        # keep previous to avoid traveling in circle without prev
        visited = set()
        def hasCycle(node, parent):
            if node in visited:
                return True

            visited.add(node)

            for nxt in adj[node]:
                if nxt == parent:
                    continue
                if hasCycle(nxt, node):
                    return True
            return False

        if hasCycle(0, -1): 
            return False
        return len(visited) == n

