class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        res = 0
        
        while left <= right:
            mid = (left + right) // 2

            if mid ** 2 == x:
                return mid
            
            if mid ** 2 > x:
                right = mid - 1

            else:
                res = mid
                left = mid + 1
        return right