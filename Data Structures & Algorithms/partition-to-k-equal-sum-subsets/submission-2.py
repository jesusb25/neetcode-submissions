class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
            
        target = total // k
        
        # Optimization 1: Sort descending to try larger numbers first (fails faster)
        nums.sort(reverse=True)
        
        # Optimization 2: If the largest number exceeds the target, it's impossible
        if nums[0] > target:
            return False
            
        # Track the current sum of our k subsets
        subsets = [0] * k
        
        def dfs(index):
            # Base case: All numbers have been successfully placed
            if index == len(nums):
                return True
                
            for i in range(k):
                # Check if the current number can fit in the i-th subset
                if subsets[i] + nums[index] <= target:
                    subsets[i] += nums[index]
                    
                    # Move to the next number
                    if dfs(index + 1):
                        return True
                        
                    # Backtrack: remove the number if it didn't lead to a solution
                    subsets[i] -= nums[index]
                    
                    # Optimization 3: If this subset is empty and didn't work,
                    # trying other empty subsets will also fail.
                    if subsets[i] == 0:
                        break
                        
            return False
            
        return dfs(0)