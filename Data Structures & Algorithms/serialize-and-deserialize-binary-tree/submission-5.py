# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        result = []

        def dfs(node):
            if not node:
                result.append("n")
                return

            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        print(result)
        return " ".join(result)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        data = data.split()
        curr = 0
        
        def dfs():
            nonlocal curr
            if data[curr] == "n":
                curr += 1
                return
            
            val = int(data[curr])
            curr += 1
            node = TreeNode(val)
            node.left = dfs()
            node.right = dfs()
            return node


        return dfs()

