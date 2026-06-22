class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        greater = {}
        res = []

        for num in nums2:
            while stack and stack[-1] < num:
                key = stack.pop()
                greater[key] = num
            stack.append(num)
        
        for num in nums1:
            if num not in greater:
                res.append(-1)
            else:
                res.append(greater[num])
        return res


                

