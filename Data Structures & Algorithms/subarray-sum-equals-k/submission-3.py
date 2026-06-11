class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = currSum = 0
        # prefix sums to how many times they appear
        prefixSums = defaultdict(int)
        prefixSums[0] = 1 # since this mean curr sum itself is valid

        for num in nums:
            currSum += num
            diff = currSum - k

            if diff in prefixSums:
                res += prefixSums[diff]
            
        
            prefixSums[currSum] += 1
            

        return res