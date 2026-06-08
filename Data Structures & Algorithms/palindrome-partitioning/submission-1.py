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

        def dfs(left):
            if left == len(s):
                result.append(path[:])
            
            for right in range(left + 1, len(s) + 1):
                new_pal = s[left : right]
                if new_pal == new_pal[::-1]:
                    path.append(new_pal)
                    dfs(right)
                    path.pop()


        
        dfs(0)
        return result
        

        