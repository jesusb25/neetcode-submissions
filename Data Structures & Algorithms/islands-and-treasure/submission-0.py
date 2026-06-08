class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # start q with all treasures [row, col, dist]
        # track seen
        # bfs, marking as we go
        if not grid:
            return
            
        q = deque()
        seen = set()
        ROWS = len(grid)
        COLS = len(grid[0])

        dirs = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append([i, j, 0])
                if grid[i][j] == -1:
                    seen.add((i, j))
        
        while q:
            row, col, dist = q.popleft()

            # stop for all nonvalid nodes
            if (min(row, col) < 0 or 
            row == ROWS or
            col == COLS or
            (row, col) in seen):
                continue
            
            grid[row][col] = dist
            seen.add((row, col))

            for dx, dy in dirs:
                q.append([row + dx, col + dy, dist + 1])


            







        