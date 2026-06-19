class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = Counter(nums)

        for key, count in counter.items():
            if count % 2 != 0:
                return False
            
        return True