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
            if len(seen) == len(word):
                return True
            
            neighbors = [
            [row + 1, col],
            [row - 1, col],
            [row, col - 1],
            [row, col + 1],
            ]

            for next_row, next_col in neighbors:
                if 0 <= next_row < ROWS and 0 <= next_col < COLS:
                    if board[next_row][next_col] != word[len(seen)]:
                        continue
                    if (next_row, next_col) in seen:
                        continue
                    seen.add((next_row, next_col))
                    if dfs(next_row, next_col): return True
                    seen.remove((next_row, next_col))

            return False
                
    
        for i in range(ROWS):
            for j in range(COLS):
                # only kick off search when start is correct
                if board[i][j] == word[0]:
                    seen.add((i, j))
                    if dfs(i, j): return True
                    seen.remove((i, j))
        return False



        


        
        
    

        