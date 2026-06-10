class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pres_left = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for dst, src in prerequisites:
            pres_left[dst] += 1
            adj[src].append(dst)

        q = deque()
        for course in range(numCourses):
            if pres_left[course] == 0:
                q.append(course)
        path = []

        while q:
            course = q.popleft()
            path.append(course)

            for nxt in adj[course]:
                pres_left[nxt] -= 1
                if pres_left[nxt] == 0:
                    q.append(nxt)
        
        return path if len(path) == numCourses else []