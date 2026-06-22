class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = deque()
        ROWS = len(board)
        COLS = len(board[0])

        free = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or
                r == ROWS - 1 or
                c == 0 or
                c == COLS - 1) and board[r][c] == "O":
                    q.append((r, c))
                    free.add((r, c))
        
        while q:
            r, c = q.popleft()

            free.add((r, c))

            for dx, dy in dirs:
                nr, nc = r + dx, c + dy

                if min(nr, nc) < 0 or nc == COLS or nr == ROWS or board[nr][nc] == "X" or (nr, nc) in free:
                    continue
                q.append((nr, nc))
        

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in free:
                    board[r][c] = "X"




        

                