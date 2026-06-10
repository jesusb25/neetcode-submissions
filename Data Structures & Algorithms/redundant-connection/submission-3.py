class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]
        
        def findRoot(node):
            if parent[node] == node:
                return node
            return findRoot(parent[node])
        
        for src, dst in edges:
            print(parent)
            dst_root = findRoot(dst)
            src_root = findRoot(src)
            if src_root == dst_root:
                return [src, dst]
            
            parent[src_root] = dst_root
        return [-1, -1]
            
