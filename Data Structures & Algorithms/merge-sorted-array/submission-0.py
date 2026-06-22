class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        write = m
        for i in range(n):
            nums1[write] = nums2[i]
            write += 1
        nums1.sort()
