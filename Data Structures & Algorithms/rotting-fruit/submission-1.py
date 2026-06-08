class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        result = 0
        # rotten fruit fruit bfs starting with initials
        q = deque() # [row, col, min]
        ROWS = len(grid)
        COLS = len(grid[0])
        # shortest path from nodes

        # add rotten, bfs around to rot more until no more to rot


        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append([row, col, 0])
        
        while q:
            row, col, minute = q.popleft()
            result = max(result, minute)

            neighbors = [
                [row + 1, col],
                [row - 1, col],
                [row, col + 1],
                [row, col - 1]
            ]

            for new_r, new_c in neighbors:
                if min(new_r, new_c) < 0:
                    continue
                
                if new_r == ROWS or new_c == COLS:
                    continue
                
                if grid[new_r][new_c] != 1:
                    continue
                
                grid[new_r][new_c] = 2
                q.append([new_r, new_c, minute + 1])


        
        # if any fruit is left unrotten, return -1
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    return -1
        return result