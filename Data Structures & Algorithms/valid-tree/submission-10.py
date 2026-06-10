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
        def dfs(node, parent):
            # if cycle return false
            if node in visited:
                return False

            # visit curr node
            visited.add(node)

            # attempt path thats not neighbor
            for nxt in adj[node]:
                if nxt == parent:
                    continue
                if not dfs(nxt, node):
                    return False

            return True

        # since nodes shoudl be connected can start anywhere
        # if start anywhere and 
        return dfs(0, -1) and len(visited) == n