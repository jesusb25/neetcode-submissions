class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # can we assume that nums will only have nums yes
        # can we assume nums has values - no 
        # can we assume length - no
        # Time O(N) Space O(N)

        seen = set()

        # go through the entire array
        for num in nums:
        # if weve seen the current num, return True
            if num in seen:
                return True

            # if we havent seen it then add it to the seen dict
            seen.add(num)

        # return False if none seen before
        return False
        