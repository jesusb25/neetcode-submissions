class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        dirs = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        ROWS, COLS = len(grid), len(grid[0])


        def dfs(row, col):
            
            if (min(row, col) < 0 or
            row == ROWS or 
            col == COLS or
            grid[row][col] == 0):
                return 0
            
            total = 1
            grid[row][col] = 0

            for dr, dc in dirs:
                total += dfs(row + dr, col + dc) 

            return total
        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
                    
        return res

