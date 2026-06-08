class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 2d grid board
        # looking for word
        # build a word in all four directions
        # only build when next options makes sense
        # if word is complete return True
        # cannot use same cell twice, set of indices?
        # use length as index

        # 1. setup seen so far
        # 2. call dfs for every possibel start cell
        # 3. dfs, base case when seen is as long as word
        # 4. curr position tracked in dfs
        if not word:
            return True

        seen = set() # (x, y)
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(row, col):
            # check success
  
            if len(seen) == len(word):
                return True
            
            # check violations
            if (min(row, col) < 0 or
            row == ROWS or
            col == COLS or
            (row, col) in seen or
            board[row][col] != word[len(seen)]):
                return False

            # current decision (always include)
            seen.add((row, col))

            # attempt options
            neighbors = [
            [row + 1, col],
            [row - 1, col],
            [row, col - 1],
            [row, col + 1],
            ]
            for next_row, next_col in neighbors:
                    if dfs(next_row, next_col): return True
            
            # remove decision
            seen.remove((row, col))
            return False
                
    
        for i in range(ROWS):
            for j in range(COLS):
                # only kick off search when start is correct
                if board[i][j] == word[0]:
                    if dfs(i, j): return True
        return False



        


        
        
    

        