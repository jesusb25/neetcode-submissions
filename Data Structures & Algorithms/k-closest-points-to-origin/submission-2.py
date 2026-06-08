class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # max_heap and add points, when k length pop if next point is closer
        max_heap = [] # [-distance, [x, y]]
        for x, y in points:
            distance = x**2 + y**2
            # if k then only add closer point
            if len(max_heap) == k:
                furthest_d = -max_heap[0][0]
                if distance < furthest_d:
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, [-distance, [x, y]])
            else:
                heapq.heappush(max_heap, [-distance, [x, y]])
        result = []
        while max_heap:
            result.append(heapq.heappop(max_heap)[1])
        return result



        