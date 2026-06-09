class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # go from outside O to inside O
        # anything not in outside in access, mark as X
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1),]
        ROWS, COLS = len(board), len(board[0])
        free = set()
        def dfs(row, col):            
            # process by adding to seen
            # attempt traversal to other Os
            free.add((row, col))

            for dx, dy in dirs:
                nr, nc = row + dx, col + dy

                if (min(nr, nc) == -1 or 
                nr == ROWS or nc == COLS or
                (nr, nc) in free or
                board[nr][nc] != "O"):
                    continue

                dfs(nr, nc)

            
        
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or r == ROWS - 1:
                    if board[r][c] == "X":
                        continue
                    dfs(r, c)
                elif c == 0 or c == COLS - 1:
                    if board[r][c] == "X":
                        continue
                    dfs(r, c)
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in free:
                    board[r][c] = "X"


        

