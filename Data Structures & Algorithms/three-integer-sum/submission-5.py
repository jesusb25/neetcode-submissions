class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        seen = set()        

        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triple = tuple(sorted([nums[i], nums[j], nums[k]]))
                        if triple not in seen:
                            seen.add(triple)
                            result.append(list(triple))
        return result