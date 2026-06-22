class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        res = []

        graph = defaultdict(dict)
        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1/val
        
        # check all combos against other combos
        # b/c * a/b  = a/c
        for b in graph:
            for a in graph[b]:
                for c in graph[b]:
                    if c not in graph[a]:
                        graph[a][c] = graph[b][c] * graph[a][b]
                        # graph[c][a] = 1 / graph[a][c]
        
        for u, v in queries:
            if u in graph and v in graph[u]:
                res.append(graph[u][v])
            else:
                res.append(-1)
        return res


