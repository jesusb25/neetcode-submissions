class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap_a = [] # process, i
        heap_p = [] # start, process, i

        for i, task in enumerate(tasks):
            start, time = task
            heapq.heappush(heap_p, [start, time, i])

        curr = 0
        res = []
        while heap_a or heap_p:
            while heap_p and curr >= heap_p[0][0]:
                start, process, i = heapq.heappop(heap_p)
                heapq.heappush(heap_a, [process, i])
            
            if heap_a:
                # process next task
                time, i = heapq.heappop(heap_a)
                res.append(i)
                curr += time
            elif heap_p:
                # wait until nearest time
                curr = heap_p[0][0]
        return res
            
            


