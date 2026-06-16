class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = []
        # [-2, -2, 1, -4, -2, -3]
        total = 0
        for num in nums:
            total += num
            self.sums.append(total)
        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0: 
            return self.sums[right]
        else:
            return self.sums[right] - self.sums[left - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)