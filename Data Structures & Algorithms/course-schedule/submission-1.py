class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # indegree[i] = number of prerequisites course i still needs
        indegree = [0] * numCourses
        # adjacency list: adj[prereq] = list of courses that depend on prereq
        adj = [[] for _ in range(numCourses)]

        # Build the graph.
        # prerequisites[i] = [a, b] means "b must be taken before a".
        # So b is the prerequisite (source) and a is the course (destination).
        for src, dst in prerequisites:   # src = prerequisite, dst = course that needs it
            indegree[dst] += 1          # course dst now has one more prerequisite
            adj[src].append(dst)        # src leads to dst (edge src -> dst)

        # Start with all courses that have no prerequisites
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish = 0                      # how many courses we've been able to "take"
        # BFS topological sort (Kahn's algorithm)
        while q:
            node = q.popleft()          # take a course with zero indegree
            finish += 1                 # mark it as completed
            # For every course that depends on this one
            for nei in adj[node]:
                indegree[nei] -= 1      # that dependency is now satisfied
                if indegree[nei] == 0:   # if a course has no remaining prerequisites
                    q.append(nei)       # it can be taken next

        # If we finished all courses, no cycle exists → return True
        return finish == numCourses