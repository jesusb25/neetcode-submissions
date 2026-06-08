class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        # 1, 1, 2

        def dfs(subset, index):
            # if index off optoins, return subset
            if index == len(nums):
                result.append(subset[:])
                return 


            # include with dfs
            subset.append(nums[index])
            dfs(subset, index + 1)
            subset.pop()

            # increase index until new num at this position
            while index + 1 != len(nums) and nums[index] == nums[index + 1]:
                index += 1
            dfs(subset, index + 1)

        dfs([], 0)
        return result

        
