class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # array of 9 sets for sub boxes
        # cols array
        # rows array
        # subBoxes[row][col]
        '''
        [[set][set][set]
        [set][set][set]
        [set][set][set]]
        '''
        subBoxDimensions = 3
        cols = [set() for i in range(len(board))]
        rows = [set() for i in range(len(board))]
        subBoxes = [[set() for y in range(subBoxDimensions)] for i in range(subBoxDimensions)]

        for row in range(len(board)):
            for col in range(len(board)):
                entry = board[row][col]
                if entry == ".":
                    continue
                
                if (entry in cols[col] or 
                entry in rows[row] or
                entry in subBoxes[row // 3][col // 3]):
                    return False
                cols[col].add(entry)
                rows[row].add(entry)
                subBoxes[row // 3][col // 3].add(entry)

        return True


                
        