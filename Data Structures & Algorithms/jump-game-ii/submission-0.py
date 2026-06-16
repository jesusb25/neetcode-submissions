class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums)
        goal = len(nums) - 1
        dp[goal] = 0

        for i in range(goal - 1, -1, -1):
            if i + nums[i] >= goal:
                dp[i] = 1 + min(dp[i : i + nums[i] + 1])
                goal = i
        return dp[0]
