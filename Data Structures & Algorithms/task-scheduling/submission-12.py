class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # prioritze frequency
        # put in order by frequency, 
        # XXYY n = 2
        # 0: x, 1: Y; 2: NONE, 3:
        q = deque() # [time, count]
        count = defaultdict(int) # task: count
        pq = [] # -counts [-2, -2]
        for task in tasks:
            count[task] += 1
        
        for task in count:
            heapq.heappush(pq, -count[task])
        t = 0

        while q or pq:
            while q and q[0][0] <= t:
                _, task_count = q.popleft()
                heapq.heappush(pq, task_count)
            
            # either process a task or idle
            t += 1
            if pq:
                neg_count = heapq.heappop(pq)
                if neg_count != -1:
                    q.append([t + n, neg_count + 1])
        return t
            
        
            
            
            