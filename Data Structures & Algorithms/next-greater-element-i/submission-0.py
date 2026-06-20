class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # map nums to index in nums2
        # pass through nums2 finding next greatest
        mapped = {} # num to next greatest

        stack = []

        for i, num in enumerate(nums2):
            while stack and stack[-1] < num:
                mapped[stack.pop()] = num
            stack.append(num)
        
        res = []
        for num in nums1:
            res.append(mapped[num] if num in mapped else -1)
        return res
