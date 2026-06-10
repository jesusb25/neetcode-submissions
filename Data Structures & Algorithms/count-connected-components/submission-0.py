class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create a list of nodes
        # when nodes are connected turn 1 false
        seen = [False] * n
        res = 0
        adj = defaultdict(list) # nodes : neighbors
        visited = set()
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for nei in adj[node]:
                seen[nei] = True
                dfs(nei)
        
        for i in range(n):
            if not seen[i]:
                dfs(i)
                res += 1
        return res
        