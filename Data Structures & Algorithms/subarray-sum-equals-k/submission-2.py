class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = currSum = 0
        # prefix sums to how many times they appear
        prefixSums = { 0 : 1 }

        for num in nums:
            currSum += num
            diff = currSum - k

            if diff in prefixSums:
                res += prefixSums[diff]
            
            if currSum not in prefixSums:
                prefixSums[currSum] = 0
            prefixSums[currSum] += 1
            

        return res