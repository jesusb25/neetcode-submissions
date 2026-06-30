class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        curRow = [1]
        prevRow = self.getRow(rowIndex - 1)

        for j in range(1, rowIndex):
            nxt = prevRow[j] + prevRow[j - 1]
            curRow.append(nxt)
        curRow.append(1)
        return curRow
