class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if not s:
            return ""
        
        stack = []
        i = 0
        while i < len(s):
            if stack and s[i] == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([s[i], 1])
            i += 1

        res = []
        for char, count in stack:
            res.extend([char] * count)
        return "".join(res)

        
        