class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        res = []

        graph = defaultdict(dict)
        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1/val
        
        # check all combos against other combos
        
        for k in graph:
            for i in graph[k]:
                for j in graph[k]:
                    if j not in graph[i]:
                        graph[i][j] = graph[i][k] * graph[k][j]
        
        for u, v in queries:
            if u in graph and v in graph[u]:
                res.append(graph[u][v])
            else:
                res.append(-1)
        return res


