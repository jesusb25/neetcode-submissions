class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        ((()))
        (()())
        '''
        result = []
        
        def dfs(open, close, par):
            if open == close == n:
                result.append(par[:])
                return
            
            if close > open or open > n:
                return
            
            new_open = par + "("
            dfs(open + 1, close, new_open)

            new_close = par + ")"
            dfs(open, close + 1, new_close)
        
        
        dfs(0, 0, "")
        return result

        