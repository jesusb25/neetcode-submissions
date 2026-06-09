class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # detect cycles
        adj = defaultdict(list) # course : [prereqs]
        path = set()
        visited = set()

        for course, pre in prerequisites:
            adj[pre].append(course)
        def dfs(course):
            if course in path:
                return True
            
            if course in visited:
                return False
            
            visited.add(course)
            path.add(course)

            for neighbor in adj[course]:
                if dfs(neighbor): return True
            
            path.remove(course)

            return False

        for start in list(adj):
            if dfs(start): return False
        
        return True


        


        


