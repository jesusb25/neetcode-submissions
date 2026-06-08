class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # set for respective column and row
        # 3x3 matrix of sets [row // 3][col // 3]
        row_sets = [set() for i in range(9)]
        col_sets = [set() for i in range(9)]
        three_by_three_sets = [[set() for i in range(3)] for j in range(3)]


        for row in range(9):
            for col in range(9):
                box_input = board[row][col]
                if box_input.isdigit():
                    if (box_input in row_sets[row] or
                        box_input in col_sets[col] or
                        box_input in three_by_three_sets[row//3][col//3]):
                        print(row, col, box_input)
    
                        return False
                    else:
                        row_sets[row].add(box_input)
                        col_sets[col].add(box_input)
                        three_by_three_sets[row//3][col//3].add(box_input)
        return True