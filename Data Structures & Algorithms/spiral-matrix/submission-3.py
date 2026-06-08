class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        left = top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1

        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                result.append(matrix[top][i])

            for i in range(top + 1, bottom + 1):
                result.append(matrix[i][right])

            if top < bottom and left < right:
                for i in range(right - 1, left - 1, -1):
                    result.append(matrix[bottom][i])

                for i in range(bottom - 1, top, -1):
                    result.append(matrix[i][left])

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return result