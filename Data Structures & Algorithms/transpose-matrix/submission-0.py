class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        col = len(matrix[0])
        result = [[0]*rows for _ in range(col)]

        for i in range(rows):
            for j in range(col):
                result[j][i] = matrix[i][j]
        return result

        