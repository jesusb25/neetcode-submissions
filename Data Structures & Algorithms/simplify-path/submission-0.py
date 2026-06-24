class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        
        stack = []
        for entry in path:
            if not entry:
                continue
            
            if entry == ".":
                continue
            elif entry == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(entry) 

            
        return "/" + "/".join(stack)