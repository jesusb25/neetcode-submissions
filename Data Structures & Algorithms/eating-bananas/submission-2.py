class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # minimize hours by eating max(piles) = k
        # min integer k within h hours
        # 1 - max search for k
        
        left = 1
        right = max(piles)

        def evaluate_hours(piles, k, h):
            total = 0
            for pile in piles:
                total += math.ceil(pile / k)
            return total


        while left < right:
            middle  = (left + right) // 2
            if evaluate_hours(piles, middle, h) > h:
                left = middle + 1
            else:
                right = middle
        
        return left