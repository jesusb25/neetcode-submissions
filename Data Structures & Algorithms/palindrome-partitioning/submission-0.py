class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        go though all indices, chop or skip at each index making sure we always
        have palindrom
        aab
        '''


        # store results
        # path store that is appended copy

        # use index to check options, if at end, made a subset

        # check options by chopping string, checking palindrome, adding to path and continuing

        result = []
        path = []

        def dfs(candidates):
            if not candidates:
                result.append(path[:])
            
            for i in range(1, len(candidates) + 1):
                new_pal, rest = candidates[:i], candidates[i:]
                if new_pal == new_pal[::-1]:
                    path.append(new_pal)
                    dfs(rest)
                    path.pop()


        
        dfs(s)
        return result
        

        