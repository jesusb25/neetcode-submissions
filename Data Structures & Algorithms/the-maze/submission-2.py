class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if not maze or not maze[0]:
            return start == destination
        seen = set()

        q = deque([start])
    
        def moveLeft(r, c):
            while c != 0 and maze[r][c - 1] != 1:
                c -= 1
            return [r, c] 

        def moveRight(r, c):
            while c != len(maze[0]) - 1 and maze[r][c + 1] != 1:
                c += 1
            return [r, c] 

        def moveUp(r, c):
            while r != 0 and maze[r - 1][c] != 1:
                r -= 1
            return [r, c] 

        def moveDown(r, c):
            while r != len(maze) - 1 and maze[r + 1][c] != 1:
                r += 1
            return [r, c] 

        
        while q:
            row, col = q.popleft()
            if [row, col] == destination:
                return True
            if (row, col) in seen:
                continue
            seen.add((row, col))

            q.append(moveLeft(row, col))
            q.append(moveRight(row, col))
            q.append(moveUp(row, col))
            q.append(moveDown(row, col))


            
            

        return False

