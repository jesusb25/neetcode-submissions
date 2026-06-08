class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # go through each row, grid
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        res = 0

            
        def explore():
            dirs = [[1, 0], [-1, 0], [0, -1], [0, 1]]
            while q:
                row, col = q.popleft()

                if (min(row, col) < 0 or
                row == ROWS or
                col == COLS or
                grid[row][col] == "0"):
                    continue
                
                grid[row][col] = "0"


                for dx, dy in dirs:
                    q.append([row + dx, col + dy])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    res += 1
                    q.append([i, j])
                    explore()
        return res


        # bfs marking land
        # return num of bfs runs