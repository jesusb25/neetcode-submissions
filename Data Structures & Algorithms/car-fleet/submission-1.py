class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # [5 seconds, 2.5 seconds, ]
        pq = []
        for s, p in zip(speed, position):
            heapq.heappush(pq, (p, s))
        
        stack = []

        while pq:
            p, s = heapq.heappop(pq)
            time = (target - p) / s
            while stack and stack[-1] <= time:
                stack.pop()

            stack.append(time)
    
        return len(stack)
                
                