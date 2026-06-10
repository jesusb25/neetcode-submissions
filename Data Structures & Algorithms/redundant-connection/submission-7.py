class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        parent = [i for i in range(N + 1)]
        rank = [1] * (N + 1)

        def findParent(node):
            if parent[node] != node:
                parent[node] = findParent(parent[node])
            return parent[node]

        def union(n1, n2):
            p1, p2 = findParent(n1), findParent(n2)
            # if same paernts, nodes are already connected
            if p1 == p2: 
                return False

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] = rank[p2]
            else:
                parent[p1] = p2
                rank[p2] = rank[p1]
            return True
        
        for a, b in edges:
            if not union(a, b):
                return [a, b]
                
        return [-1, -1]
            

