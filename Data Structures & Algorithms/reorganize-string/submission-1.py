class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        res = ""

        # heap plus cooldown q
        heap = []
        for key, num in count.items():
            heap.append([-num, key])
        
        heapq.heapify(heap)
        last = None

        while heap:
            num, char = heapq.heappop(heap)
            res += char

            if last:
                heapq.heappush(heap, last)
            
            if num != -1:
                last = [num + 1, char]
            else:
                last = None

            
        if last:
            return ""
        else:
            return res

            



