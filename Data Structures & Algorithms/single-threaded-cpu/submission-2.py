class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # sort by enqueue time
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()

        res = []
        heap = []
        curr = 0
        n = len(tasks)
        i = 0

        while i < n or heap:
            # enqueue all possible tasks
            while i < n and tasks[i][0] <= curr:
                _, p, task_i = tasks[i]
                i += 1
                heapq.heappush(heap, [p, task_i])

            # process all possible tasks
            if heap:
                process, task_i = heapq.heappop(heap)
                curr += process
                res.append(task_i)
            
            # move up to next time
            if i < n and not heap:
                curr = max(curr, tasks[i][0])
                
        return res
