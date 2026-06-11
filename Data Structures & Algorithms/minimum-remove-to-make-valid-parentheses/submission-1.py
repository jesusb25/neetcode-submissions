class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        Input: s = "x(y)z("

        Output: "x(y)z"
        '''
        stack = [] # append open

        s = list(s)

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack: 
                    stack.pop()
                else:
                    s[i] = ""
        
        while stack:
            inv_i = stack.pop()
            s[inv_i] = ""

        return "".join(s)