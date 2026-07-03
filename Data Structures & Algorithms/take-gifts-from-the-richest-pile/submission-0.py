import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-g for g in gifts]
        heapq.heapify(heap)

        for i in range(k):
            curr = -heapq.heappop(heap)
            heapq.heappush(heap, -int(math.sqrt(curr)))
        
        return -sum(heap)

