class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        Input: s = "x(y)z("

        Output: "x(y)z"
        '''
        stack = [] # indices of "("
        include = [False] * len(s)

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack and s[stack[-1]] == "(":
                    include[stack[-1]] = True
                    include[i] = True
                    stack.pop()
            else:
                include[i] = True
        
        res = []
        for i, char in enumerate(s):
            if include[i]:
                res.append(char)
        return "".join(res)