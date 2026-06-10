class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i + 1 for i in range(n)]
        
        def findRoot(node):
            if parent[node - 1] == node:
                return node
            return findRoot(parent[node - 1])
        
        for src, dst in edges:
            print(parent)
            dst_root = findRoot(dst)
            src_root = findRoot(src)
            if src_root == dst_root:
                return [src, dst]
            
            parent[src_root - 1] = dst_root
        return [-1, -1]
            
