class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        productFromLeft = 1
        for num in nums:
            result.append(productFromLeft)
            productFromLeft *= num
        
        print(result)

        productFromRight = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= productFromRight
            productFromRight *= nums[i]
        
        return result

        