class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        perm = []

        def dfs(perm, options):
            if not options:
                result.append(perm.copy())

            for i, option in enumerate(options):
                next_options = options[ : i] + options[i + 1 :]
                perm.append(option)
                dfs(perm, next_options)
                perm.pop()
            
        dfs([], nums)
        return result
        