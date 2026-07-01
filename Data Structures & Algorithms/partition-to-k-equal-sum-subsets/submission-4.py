class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        
        nums.sort(reverse=True)
        

        subsets = [0] * k
        target = sum(nums) / k

        def dfs(i):
            if i == len(nums):
                return True
            
            for j in range(k):
                if subsets[j] + nums[i] <= target:
                    subsets[j] += nums[i]
                    if dfs(i + 1):
                        return True
                    subsets[j] -= nums[i]
                
                    if subsets[j] == 0:
                        break
            return False
        return dfs(0)