class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        q = deque()
        visited = set()
        res = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(row, col):
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            if (row, col) in visited or grid[row][col] == "0":
                return
            
            visited.add((row, col))
            
            for dx, dy in dirs:
                nr, nc = row + dx, col + dy
                if not (0 <= nr < ROWS):
                    continue
                
                if not (0 <= nc < COLS):
                    continue
                dfs(nr, nc)
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    res += 1
                    dfs(r, c)
        return res


