class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create sets for each box
        # create set for each col
        # create set for each row
        # go through and validate no duplicates exist in any valid row, col or box
        ROWS = len(board)
        COLS = len(board[0])
        rows = [set() for i in range(ROWS)]
        cols = [set() for i in range(COLS)]
        sub_boxes = [[set() for j in range(3)] for i in range(3)]


        for row in range(ROWS):
            for col in range(COLS):
                entry = board[row][col]
                if entry == ".":
                    continue
                
                if (entry in rows[row] or
                entry in cols[col] or
                entry in sub_boxes[row // 3][col // 3]):
                    return False
                
                rows[row].add(entry)
                cols[col].add(entry)
                sub_boxes[row // 3][col // 3].add(entry)


        return True