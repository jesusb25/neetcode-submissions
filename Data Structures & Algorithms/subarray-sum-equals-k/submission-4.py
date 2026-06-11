class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currSum = 0
        prefix = defaultdict(int)
        prefix[0] += 1
        # 0 : 1
        # [2, 1, 2, 2]
        for num in nums:
            currSum += num
            diff = currSum - k

            if diff in prefix:
                res += prefix[diff]
            prefix[currSum] += 1
        return res