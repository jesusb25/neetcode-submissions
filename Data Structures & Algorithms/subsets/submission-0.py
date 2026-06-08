class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        result = []

        # base case, index out return options so far
        # dfs include exclude
        def dfs(options, index, curr):
            if index == len(options):
                result.append(curr.copy())
                return
            
            curr.append(options[index])
            dfs(options, index + 1, curr)
            curr.pop()
            dfs(options, index + 1, curr)

        dfs(nums, 0, [])
        return result
        