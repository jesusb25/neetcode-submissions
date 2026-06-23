class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort()

        res, heap = [], []
        i, time = 0, 0
        n = len(tasks)

        while heap or i < n:
            # enqueue all possible tasks
            while i < n and tasks[i][0] <= time:
                _, p, index = tasks[i]
                heapq.heappush(heap, [p, index])
                i += 1
            
            # if none enqueue push time forward
            if not heap:
                time = tasks[i][0]
            # otherwise start processing
            else:
                p, index = heapq.heappop(heap)
                time += p
                res.append(index)

        return res