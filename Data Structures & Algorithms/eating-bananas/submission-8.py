class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right

        def total_hours(piles, k):
            total = 0
            for pile in piles:
                total += math.ceil(pile / k)
            return total

        while left <= right:
            middle = (left + right) // 2
            hours = total_hours(piles, middle)

            if hours > h:
                left = middle + 1
            else:
                result = middle
                right = middle - 1

        return result
