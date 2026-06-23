class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        prefix = [0]

        # prefix of each window
        for num in nums:
            prefix.append(num + prefix[-1])
        
        res = 0

        # try every combo of subarrays
        for i in range(n + 1):
            for j in range(i, n):
                if prefix[j + 1] - prefix[i] == goal:
                    res += 1
        return res