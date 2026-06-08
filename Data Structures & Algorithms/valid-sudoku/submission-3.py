class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        subBoxes = [[set() for i in range(3)] for i in range(3)]

        for row in range(9):
            for col in range(9):
                entry = board[row][col]
                if entry == '.':
                    continue
                if (entry in rows[row] or
                entry in cols[col] or 
                entry in subBoxes[row // 3][col // 3]):
                    return False
                rows[row].add(entry)
                cols[col].add(entry)
                subBoxes[row // 3][col // 3].add(entry)


        return True