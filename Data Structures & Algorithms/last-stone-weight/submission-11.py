class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heap, pop and append negative num until done
        # return remainder or none

        if not stones:
            return 0
        
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            if stone1 != stone2:
                heapq.heappush(stones, stone1 - stone2)
            

        return -stones[0] if stones else 0
