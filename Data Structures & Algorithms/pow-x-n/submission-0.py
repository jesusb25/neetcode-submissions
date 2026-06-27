class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        res = 1

        for i in range(abs(n)):
            if n < 0:
                res /= x
            else:
                res *= x


            
        return res