class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        read = 0
        write = 0


        while read < len(nums):
            digit = nums[read]
            nums[write] = digit
            write += 1
            start = read
            if write == len(nums):
                break

            while read < len(nums) and nums[read] == digit:
                read += 1
            
            # no duplicates
            if read == start + 1:
                continue
            # write two occs at most
            else:
                nums[write] = digit
                write += 1
            
        return write
            
            







