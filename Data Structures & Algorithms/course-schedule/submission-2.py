class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # count num needed still for index n class
        pres = [0] * numCourses 
        # adj list of neighbors
        adj = [[] for i in range(numCourses)]
        for dst, src in prerequisites:
            pres[dst] += 1
            adj[src].append(dst)
        
        q = deque() # bfs all starts
        # start with all elgible classes
        for i in range(numCourses):
            if pres[i] == 0:
                q.append(i)
            
        
        finished = 0
        while q:
            course = q.popleft()
            finished += 1
        
            for nxt in adj[course]:
                pres[nxt] -= 1
                if pres[nxt] == 0:
                    q.append(nxt)
        return finished == numCourses

        