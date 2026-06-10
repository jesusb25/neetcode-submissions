class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # count num needed still for index n class
        presLeft = [0] * numCourses 
        # adj list of neighbors
        adj = [[] for i in range(numCourses)]
        for dst, src in prerequisites:
            presLeft[dst] += 1
            adj[src].append(dst)
        
        q = deque() # bfs all starts
        # start with all elgible classes
        for i in range(numCourses):
            if presLeft[i] == 0:
                q.append(i)
            
        
        finished = 0
        while q:
            course = q.popleft()
            finished += 1
        
            # remove 1 from prereqs left
            for nxt in adj[course]:
                presLeft[nxt] -= 1
                # take eligible courses
                if presLeft[nxt] == 0:
                    q.append(nxt)

        return finished == numCourses

        