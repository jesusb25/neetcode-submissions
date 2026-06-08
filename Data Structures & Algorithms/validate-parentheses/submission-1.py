class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for char in s:
            if not char in pairs:
                stack.append(char)
            else:
                if not stack or pairs[char] != stack[-1]:
                    return False
                stack.pop()
        return len(stack) == 0 


        