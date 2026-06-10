class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [1] * (n + 1)
        
        def find(node):
            # Path compression: make node point directly to root
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(src, dst):
            src_root = find(src)
            dst_root = find(dst)
            
            if src_root == dst_root:
                return False  # already in same set → cycle
            
            # Union by rank: attach smaller tree under larger
            if rank[src_root] > rank[dst_root]:
                parent[dst_root] = src_root
                rank[src_root] += rank[dst_root]
            else:
                parent[src_root] = dst_root
                rank[dst_root] += rank[src_root]
            return True
        
        for src, dst in edges:
            if not union(src, dst):
                return [src, dst]
        
        return [-1, -1]