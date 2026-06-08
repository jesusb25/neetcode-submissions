class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # create n x n board

        # track which rows, cols and diaganols are still legal
        # remove from legal options as we go
        solutions = []
        ROWS = COLS = n
        locs = set() # (x, y) of each placed queen
        row_picked = [False for i in range(ROWS)]
        col_picked = [False for i in range(COLS)]
        left_diag = {row - col for row in range(ROWS) for col in range(COLS)}
        right_diag = set([i for i in range((n - 1) * 2 + 1)])

        def dfs(queens, row_index):
            if queens == n:
                solutions.append(list(locs))
                return
            
            for row in range(row_index, ROWS):
                if row_picked[row]:
                    continue
                for col in range(COLS):
                    # col or row occupied
                    if col_picked[col]:
                        continue
                    
                    # right diag occupied (sum)
                    if col + row not in right_diag:
                        continue

                    # left diag check
                    if row - col not in left_diag:
                        continue
                    
                    # pick and explore 
                    row_picked[row], col_picked[col] = True, True
                    left_diag.remove(row - col)
                    right_diag.remove(col + row)
                    locs.add((row, col))

                    dfs(queens + 1, row + 1)

                    # unpick
                    row_picked[row], col_picked[col] = False, False
                    left_diag.add(row - col)
                    right_diag.add(col + row)
                    locs.remove((row, col))
        
        board = [["." for i in range(COLS)] for i in range(ROWS)] 
        dfs(0, 0)
        result = []

        for sol in solutions:
            new_board = [row[:] for row in board]
            for row, col in sol:
                new_board[row][col] = "Q"
            
            result.append(["".join(new_row) for new_row in new_board])
        return result
        

