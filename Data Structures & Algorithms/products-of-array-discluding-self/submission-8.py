class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force is n^2
        # [1, 2, 4, 6]
        # result = [1, 1, 2, 8]
        # result = [48, 24, 12, 8] prod_right = 48
        # go through left to right finding product from the left
        result = []
        product = 1
        for num in nums:
            result.append(product)
            product *= num

        # go through right to left finding product from left * proudct from right
        right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result
