class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # search each row
        row_sets = [set() for i in range(9)]
        # search each column
        col_sets = [set() for i in range(9)]
        # search each box
        box_sets = [[set() for i in range(3)] for j in range(3)]
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num != '.':
                    box_row = row // 3
                    box_col = col // 3
                    if num in row_sets[row] or num in col_sets[col] or num in box_sets[box_row][box_col]:
                        return False
                    else:
                        row_sets[row].add(num)
                        col_sets[col].add(num)
                        box_sets[box_row][box_col].add(num)
        return True

        