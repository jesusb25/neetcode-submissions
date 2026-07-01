class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose = {
            ")" :  "(",
            "]" :  "[",
            "}" :  "{"
        }
        
        for char in s:
            if char in openToClose:
                if not stack or stack[-1] != openToClose[char]:
                    return False
                
                stack.pop()
            else:
                stack.append(char)
        return not stack 