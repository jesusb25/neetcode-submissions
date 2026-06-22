class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        cooldown = None
        heap = [[-a, "a"], [-b, 'b'], [-c, 'c']]
        heapq.heapify(heap)
        res = []

        while heap:
            count, nxt_char = heapq.heappop(heap)
            if count == 0:
                continue

            res.append(nxt_char)
            count += 1

            # handle cooldown
            if cooldown:
                heapq.heappush(heap, cooldown)
            cooldown = None

            # add next
            if len(res) > 1 and res[-2] == res[-1] == nxt_char:
                cooldown = [count, nxt_char]
            else:
                heapq.heappush(heap, [count, nxt_char])
            
            
        return "".join(res)